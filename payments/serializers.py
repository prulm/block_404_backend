from rest_framework import serializers

from accounts.serializers import CustomUserSerializer
from houses.serializers import *
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
        fields = ( 'payment', 'paid_by', 'amount', 'verified', 'total_paid', 'payment_progress')

class HousePaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePayment
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    residents = ResidentSerializer(many=True)
    owner = CustomUserSerializer()
    house_payments = HousePaymentSerializer(many=True)
    house_attachments = HouseAttachmentSerializer(many=True)
    house_pictures = HousePictureSerializer(many=True)
    class Meta:
        model = House
        fields = ('floor', 'floorCode', 'description', 'bedrooms', 'squareMeter', 'status', 'house_attachments', 'house_pictures', 'owner', 'residents', 'house_payments')

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class BuildingExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingExpense
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    creator = ResidentSerializer()
    class Meta:
        model = Event
        exclude = ('building')

class EventCreateSerializer(serializers.ModelSerializer):
    class Meta(EventSerializer.Meta):
        fields = '__all__'