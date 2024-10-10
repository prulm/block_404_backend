from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .serializers import *

class CommitteeCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = CreateCommitteeSerializer
