from rest_framework import serializers
from .models import *

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ('building')