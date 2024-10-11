from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from .models import *

class ResidentSerializer(serializers.ModelSerializer):
    resident = CustomUserSerializer()
    class Meta:
        model = Resident
        exclude = ['house']

class ResidentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    residents = ResidentSerializer(many=True)
    owner = CustomUserSerializer()

    class Meta:
        model = House
        fields = ('floor', 'floorCode', 'description', 'bedrooms', 'squareMeter', 'status', 'owner', 'residents')