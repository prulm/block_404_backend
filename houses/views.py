from django.db import models
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import permissions
from buildings.serializers import BuildingDetailSerializer
from .serializers import *

class HouseCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = HouseSerializer

class HouseListView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = BuildingDetailSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Building.objects.filter(models.Q(houses__owner = user) | models.Q(houses__residents = user.id)).distinct()