import jwt
from django.contrib.auth import login
from django.http import JsonResponse
from rest_framework import (status, permissions, generics)
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shop import settings
from .models import Attribute, Category, Product, UserAccount
from .serializers import (CategoryListSerializer, UserSerializer, AtributeSerializer, ProductSerializer)
from .utils.controllers.otp_controller import Otp
from .utils.jwt.authentication import JWTAuthentication
from .utils.jwt.token_util import generate_access_token, generate_refresh_token, refresh_access_token


class ValidatePhoneSendOTP(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        phone: str = request.data.get('phone_number')
        return Response(Otp.validate_phone_send_otp(phone_number=phone))


class ValidateOTPLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        phone: str = request.data.get('phone_number')
        otp_sent: str = request.data.get('otp')
        validate_info = Otp.check_otp(phone_number=phone, otp_sent=otp_sent)

        if validate_info['status'] is False:
            return JsonResponse({'status': status.HTTP_400_BAD_REQUEST,
                                 'detail': validate_info['detail']})

        user = UserAccount.objects.filter(phone_number=phone).first()
        serialized_user = UserSerializer(user).data

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        response.data = {
            'access_token': access_token,
            'user': serialized_user,
        }
        login(request, user)
        return response


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user})


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_obtain_tokens(request):
    response = Response()
    refresh_token_payload = jwt.decode(
        request.COOKIES.get("refresh_token"), settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])

    user = UserAccount.objects.filter(phone_number=refresh_token_payload.get('phone_number')).first()
    serialized_user = UserSerializer(user).data
    response.data = {
        'access_token': refresh_access_token(request.COOKIES.get("refresh_token")),
        'user': serialized_user,
    }
    response.set_cookie(key='refresh_token', value=generate_refresh_token(user), httponly=True)
    return response


class CreateUserAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        user = request.POST.dict()
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # region
    class CategoryListView(generics.ListAPIView):
        queryset = Category.objects.order_by('position')
        serializer_class = CategoryListSerializer

    class AtributeView(APIView):
        def get(self, request, idcat):
            attr = Attribute.objects.prefetch_related('values').filter(category__id=idcat)
            serializer = AtributeSerializer(attr, many=True)
            return Response(serializer.data)

    class ProductView(APIView):
        def get(self, request, pk):
            products = Product.objects.filter(category__id=pk)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
    # endregion
