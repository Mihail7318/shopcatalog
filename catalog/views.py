from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import CategoryListSerializer, AttributeListSerializer
from .models import Category, Attribute


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.order_by('position')
    serializer_class = CategoryListSerializer



class AttributeListView(APIView):
    def get(self, request, id_cat):
        #category_id = request.GET.get("id_cat", "1")
        attr = Attribute.objects.filter(category__id=id_cat)
        serializer = AttributeListSerializer(attr, many=True)
        return Response(serializer.data)
