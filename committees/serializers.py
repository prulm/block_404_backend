from rest_framework import serializers
from .models import *

class CommitteeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Committee
        fields = '__all__'