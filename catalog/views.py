from functools import reduce

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from django.db.models import Q
import operator

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
        query = self.request.GET.get('q')
        brand = self.request.GET.get('brand')
        q_list = Q(category__id=pk)
        if not brand:
            print("none")
        else:
            q_list.add(Q(brand=brand), Q.AND)
        products = Product.objects.all().filter(q_list)

        if query:
            decoded = json.loads(query)
            for k, v in decoded.items():
                vs = str(v)
                if vs.find("-") != -1:
                    min = vs[0:vs.find("-")]
                    max = vs[vs.find("-")+1:len(vs)]
                    print(min)
                    print(max)
                    products = products.filter(Q(value__value__gte=min) & Q(value__value__lte=max) & Q(value__attribute__id=k))
                else:
                    products = products.filter(Q(value__value=v) & Q(value__attribute__id=k))
        serializer = ProductSerializer(products, many=True)
        print(products.query)
        return Response(serializer.data)


