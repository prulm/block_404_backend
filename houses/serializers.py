from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from .models import *

class ResidentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Resident
        fields = ('isOwner', 'isHead', 'isActive', 'user')

class ResidentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = '__all__'

class ResidentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        exclude = ['user']

class HouseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class HouseGenericSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer()
    class Meta:
        model = House
        fields = ('floor', 'floorCode', 'description', 'bedrooms', 'squareMeter', 'status', 'owner')

class ResidentDetailSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    house = HouseGenericSerializer()

    class Meta:
        model = Resident
        fields = ('isHead', 'isOwner', 'isActive', 'user', 'house')