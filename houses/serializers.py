from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from .models import *

class ResidentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Resident
        fields = ('user', 'isOwner', 'isHead', 'isActive')

class ResidentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = '__all__'

class ResidentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        exclude = ['resident']

class HouseSerializer(serializers.ModelSerializer):
    residents = ResidentSerializer(many=True)
    owner = CustomUserSerializer()

    class Meta:
        model = House
        fields = ('floor', 'floorCode', 'description', 'bedrooms', 'squareMeter', 'status', 'owner', 'residents')