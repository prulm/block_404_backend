from rest_framework import serializers
from committees.serializers import CommitteeSerializer
from houses.serializers import HouseSerializer
from payments.serializers import PaymentSerializer
from .models import *

class BuildingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Building
        fields = '__all__'

class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingAttachment
        fields = ('id', 'file')

class PenalitySerialier(serializers.ModelSerializer):
    class Meta:
        model = Penality
        fields = '__all__'

class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingPicture
        fields = ('id', 'picture')

class BuildingDetailSerializer(serializers.ModelSerializer):
    pictures = PicturesSerializer(many=True)
    attachments =  AttachmentsSerializer(many=True)
    committee = CommitteeSerializer(many=True)
    houses = serializers.SerializerMethodField()

    class Meta(BuildingSerializer.Meta):
        fields = ('id', 'name', 'description', 'housesPerFloor', 'floors', 'address', 'attachments', 'pictures', 'payments', 'committee', 'houses')
    
    def get_houses(self, obj):
        user = self.context['request'].user
        user_houses = obj.houses.filter(models.Q(owner=user) | models.Q(residents__user=user)).distinct()
        return HouseSerializer(user_houses, many=True).data
