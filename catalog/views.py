from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import CategoryListSerializer
from .models import Category


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.order_by('position')
    serializer_class = CategoryListSerializer

