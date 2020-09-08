from rest_framework import serializers

from .models import Category
from .models import UserAccount


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = UserAccount
        fields = ['phone_number', 'full_name']
