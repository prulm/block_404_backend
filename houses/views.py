from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import permissions
from .serializers import *

class HouseCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = HouseSerializer