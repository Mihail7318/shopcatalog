from rest_framework import serializers

from .models import Attribute, Category, Value


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = "__all__"


class AttributeListSerializer(serializers.ModelSerializer):
    value = ValueSerializer(many=True)

    class Meta:
        model = Attribute
        fields = ['name', 'value']
