from rest_framework import serializers
from committees.serializers import CommitteeSerializer
from houses.serializers import HouseSerializer
from .models import *

class BuildingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Building
        fields = '__all__'

class AttachmentsSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=True)

    class Meta:
        model = BuildingAttachment
        fields = ('id', 'file')

class PicturesSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True)

    class Meta:
        model = BuildingPicture
        fields = ('id', 'picture')

class PaymentSerializer(serializers.ModelSerializer):
    pass

# to-do:    - create house model

class BuildingDetailSerializer(serializers.ModelSerializer):
    pictures = PicturesSerializer(many=True)
    attachments =  AttachmentsSerializer(many=True)
    committee = CommitteeSerializer()
    houses = HouseSerializer(many=True)

    class Meta(BuildingSerializer.Meta):
        fields = ('id', 'name', 'description', 'housesPerFloor', 'floors', 'address', 'attachments', 'pictures', 'committee', 'houses')