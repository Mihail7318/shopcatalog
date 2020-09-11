from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Attribute, Category, Value
from .serializers import (AtributeSerializer, CategoryListSerializer,
                          ValueSerializer)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.order_by('position')
    serializer_class = CategoryListSerializer


class AtributeView(APIView):
    def get(self, request, idcat):
        attr = Attribute.objects.prefetch_related('values').filter(category__id=idcat)
        serializer = AtributeSerializer(attr, many=True)
        return Response(serializer.data)
