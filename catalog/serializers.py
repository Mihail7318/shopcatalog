from rest_framework import serializers
from phonenumber_field.modelfields import PhoneNumberField
from .models import (UserAccount, Attribute, Category, Value, Product)


class UserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(unique=True, null=False)

    class Meta(object):
        model = UserAccount
        fields = ['phone_number']


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
