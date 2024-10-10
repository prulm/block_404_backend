from rest_framework import serializers
from .models import *

class CommitteeSerializer(serializers.ModelSerializer):
    # description = serializers.CharField()

    class Meta:
        model = Committee
        exclude = ['building', 'description']

class CreateCommitteeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Committee
        fields = '__all__'