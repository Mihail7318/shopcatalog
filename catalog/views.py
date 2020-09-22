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
        price = self.request.GET.get('price')
        q_list = Q(category__id=pk)
        if price:
            pr = json.loads(price)
            if type(pr) == dict:
                if 'min' in pr.keys():
                    min = pr['min']
                    q_list.add(Q(price__gte=min), Q.AND)
                if 'max' in pr.keys():
                    max = pr['max']
                    q_list.add(Q(price__lte=max), Q.AND)
            else:
                q_list.add(Q(price=price), Q.AND)
        if brand:
            q_list.add(Q(brand=brand), Q.AND)
        if query:
            decoded = json.loads(query)
            print(decoded)
            for k, v in decoded.items():
                print(k,v)
                if type(v) == dict:
                    print("dict")
                    q_list.add(Q(value__attribute__id=k), Q.AND)
                    if 'min' in v.keys():
                        min = v['min']
                        q_list.add(Q(value__value__gte=min), Q.AND)
                    if 'max' in v.keys():
                        max = v['max']
                        q_list.add(Q(value__value__lte=max), Q.AND)
                else:
                    q_list.add(Q(value__value=v) & Q(value__attribute__id=k))
        prd = Product.objects.filter(q_list)
        serializer = ProductSerializer(prd, many=True)
        print(prd.query)
        return Response(serializer.data)


