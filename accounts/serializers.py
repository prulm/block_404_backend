from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User,
        fields = ('id', 'firstName', 'lastName', 'phone', 'email', 'password')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "groups", "user_permissions", "last_login"]