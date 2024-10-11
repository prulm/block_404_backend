from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .serializers import *

class CommitteeCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = CreateCommitteeSerializer

class CommitteeMemberAddView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        serializer.save(committee=self.request.data.get('committee'))