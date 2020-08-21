from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Attribute, Category
from .serializers import AttributeListSerializer, CategoryListSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.order_by('position')
    serializer_class = CategoryListSerializer


class AttributeListView(APIView):
    def get(self, request, id_cat):
        attr = Attribute.objects.filter(category__id=id_cat).order_by('position')
        serializer = AttributeListSerializer(attr, many=True)
        return Response(serializer.data)
