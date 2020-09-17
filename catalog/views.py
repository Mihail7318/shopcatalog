from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import (status, permissions)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Attribute, Category, Product, UserAccount
from .serializers import (CategoryListSerializer, UserSerializer, AtributeSerializer, ProductSerializer)
from .utils.controllers.otp_controller import OtpController


class ValidatePhoneSendOTP(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        phone_number: str = request.data.get('phone_number')
        return Response(OtpController.validate_phone_send_otp(phone_number=phone_number))


def val(request):
    phone_number: str = (request.GET.get('phone_number')).replace(' ', '+')
    user = authenticate(phone_number=phone_number)

    if user is not None:
        if user.validated:
            login(request, user)
            return JsonResponse({'status': status.HTTP_200_OK,
                                 'detail': 'success auth'})
        else:
            return JsonResponse({'status': status.HTTP_400_BAD_REQUEST,
                                 'detail': 'disabled account'})
    else:
        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST,
                             'detail': 'invalid login'})


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
# import jwt
#
# encoded_jwt = jwt.encode({'phone_number': cls.phone_number}, 'U*#u1u821ek213#(K', algorithm='HS256')
#         user_details = {'token': encoded_jwt}
