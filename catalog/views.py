from rest_framework import generics
from rest_framework import (status, permissions)
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.utils.otp_controller import Otp
from .models import Attribute, Category, Product
from .serializers import (CategoryListSerializer, UserSerializer, AtributeSerializer, ProductSerializer)


class CreateUserAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        user = request.POST.dict()
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ValidatePhoneSendOTP(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        phone_number: str = request.data.get('phone_number')
        return Response(Otp.validate_phone_send_otp(phone_number=phone_number))


class ValidateOTP(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        phone_number: str = request.data.get('phone_number', False)
        otp_sent: str = request.data.get('otp', False)
        return Response(Otp.validate_otp(phone_number=phone_number, otp_sent=otp_sent))

      
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
