from rest_framework import serializers
from .models import *

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'