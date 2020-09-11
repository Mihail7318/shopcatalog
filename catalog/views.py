from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Attribute, Category, Value, Product
from .serializers import (AtributeSerializer, CategoryListSerializer, ProductSerializer,
                          ValueSerializer)


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
