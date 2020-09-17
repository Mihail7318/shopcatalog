from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import (status, permissions, generics)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Attribute, Category, Product, UserAccount
from .serializers import (CategoryListSerializer, UserSerializer, AtributeSerializer, ProductSerializer)
from .utils.controllers.otp_controller import Otp


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
        validate_info = Otp.check_otp(phone, otp_sent)

        if validate_info['status'] is False:
            return JsonResponse({'status': status.HTTP_400_BAD_REQUEST,
                                 'detail': validate_info['detail']})

        user = authenticate(phone_number=phone)
        if user is None:
            return JsonResponse({'status': status.HTTP_400_BAD_REQUEST,
                                 'detail': 'invalid login'})

        login(request, user)
        return JsonResponse({'status': status.HTTP_200_OK,
                             'detail': 'success auth'})


class CreateUserAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        user = request.POST.dict()
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def testfunk(request):
    return JsonResponse({"user": request.user.id,
                         "TEXT": "BLABLABALA"})


def out(request):
    user = request.user.id
    logout(request)
    return JsonResponse({"logout": True,
                         "user": user})

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
