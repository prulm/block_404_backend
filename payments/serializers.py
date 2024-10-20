from rest_framework import serializers

from accounts.serializers import CustomUserSerializer
from houses.serializers import ResidentDetailSerializer, ResidentSerializer
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
        fields = ( 'payment', 'paid_by', 'amount', 'total_paid', 'payment_progress')

class HouseSerializer(serializers.ModelSerializer):
    residents = ResidentSerializer(many=True)
    owner = CustomUserSerializer()
    house_payments = HousePaymentSerializer(many=True)
    class Meta:
        model = House
        fields = ('floor', 'floorCode', 'description', 'bedrooms', 'squareMeter', 'status', 'owner', 'residents', 'house_payments')

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class BuildingExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingExpense
        fields = '__all__'