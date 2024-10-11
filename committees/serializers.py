from rest_framework import serializers
from .models import *

class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        exclude = ['building']

class CreateCommitteeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Committee
        fields = '__all__'