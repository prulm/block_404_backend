from rest_framework import serializers
from .models import *

class BuildingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Building
        fields = '__all__'

class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingAttachment

class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingAttachment

class PaymentSerializer(serializers.ModelSerializer):
    pass

# to-do:    - create house model

class BuildingDetailSerializer(serializers.ModelSerializer):
    pictures = PicturesSerializer(many=True)

    class Meta(BuildingSerializer.Meta):
        pass
