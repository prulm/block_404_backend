from rest_framework import serializers

from houses.serializers import ResidentDetailSerializer
from .models import *

class PenalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Penality
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    penality = PenalitySerializer()
    collector = ResidentDetailSerializer()
    class Meta:
        model = Payment
        fields = ('name', 'type', 'description', 'amount', 'deadline', 'isRecurring', 'recurrence_period', 'attachment', 'penality', 'collector')

class HousePaymentSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True)
    paid_by = ResidentDetailSerializer()
    class Meta:
        model = HousePayment