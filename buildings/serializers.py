from rest_framework import serializers
from .models import *

class BuildingCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Building