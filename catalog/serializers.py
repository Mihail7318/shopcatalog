from rest_framework import serializers

from .models import Attribute, Category, Value, Product


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ("value",)


class AtributeSerializer(serializers.ModelSerializer):
    values = ValueSerializer(many=True)

    class Meta:
        model = Attribute
        fields = ('name', 'values')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'brand', 'price', 'description')
