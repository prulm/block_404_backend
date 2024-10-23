from rest_framework.generics import  ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions
from .models import *
from .serializers import *

class PaymentCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = PaymentCreateSerializer

class EventCreateView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = EventCreateSerializer