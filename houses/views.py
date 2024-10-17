from django.db import IntegrityError, models
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import permissions, status
from buildings.serializers import BuildingDetailSerializer
from .serializers import *

class HouseCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = HouseCreateSerializer

class HouseListView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = BuildingDetailSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Building.objects.filter(models.Q(houses__owner=user) | models.Q(houses__residents=user.id)).distinct()
    
class ResidentAddView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = ResidentCreateSerializer


class ResidentActivateView(UpdateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = ResidentCreateSerializer
    queryset = Resident.objects.all()

class ResidentRegisterView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ResidentRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
         try:
             return super().create(request, *args, **kwargs)
         except IntegrityError as err:
             if 'unique constraint' in str(err):
                return Response(
                    {'Error': 'Each resident should be unique to a house.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
             else:
                raise IntegrityError(err)