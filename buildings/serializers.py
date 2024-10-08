from rest_framework import serializers
from committees.serializers import CommitteeSerializer
from houses.serializers import HouseSerializer
from .models import *

class BuildingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Building
        fields = '__all__'

class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingAttachment
        fields = ('id', 'file')

class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingPicture
        fields = ('id', 'picture')

class PaymentSerializer(serializers.ModelSerializer):
    pass

class BuildingDetailSerializer(serializers.ModelSerializer):
    pictures = PicturesSerializer(many=True)
    attachments =  AttachmentsSerializer(many=True)
    committee = CommitteeSerializer()
    houses = serializers.SerializerMethodField()

    class Meta(BuildingSerializer.Meta):
        fields = ('id', 'name', 'description', 'housesPerFloor', 'floors', 'address', 'attachments', 'pictures', 'committee', 'houses')
    
    def get_houses(self, obj):
        user = self.context['request'].user
        user_houses = obj.houses.filter(models.Q(owner=user) | models.Q(residents=user.id))
        return HouseSerializer(user_houses, many=True).data
