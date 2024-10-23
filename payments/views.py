from rest_framework.generics import  ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions
from .models import *
from .serializers import *

class PaymentCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = PaymentCreateSerializer

class PaymentListView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PaymentCreateSerializer
    
    def get_queryset(self):
        return Payment.objects.filter(building=self.kwargs['pk'])

class HousePaymentCreateView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = HousePaymentCreateSerializer()

class EventCreateView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = EventCreateSerializer

