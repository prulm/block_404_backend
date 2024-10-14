from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .serializers import *

class CommitteeCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = CreateCommitteeSerializer

class CommitteeMemberAddView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = MemberCreateSerializer

class CommitteeRuleAddView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = RuleSerializer

    def perform_create(self, serializer):
        return serializer.save(committee_id=self.request.data.get('committee'))