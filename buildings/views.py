from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework import permissions
from .serializers import *

class BuildingCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser)
    serializer_class =  BuildingSerializer
