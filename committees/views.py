from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .serializers import *

class CommitteeCreateView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = CreateCommitteeSerializer

class CommitteeMemberAddView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = MemberCreateSerializer

    def perform_create(self, serializer):
        resident_com = Resident.objects.get(user=self.request.data.get('user'))
        return serializer.save(resident=resident_com)

class CommitteeRuleAddView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = RuleSerializer

    def perform_create(self, serializer):
        return serializer.save(committee_id=self.request.data.get('committee'))
    
class CommitteeReportAddView(CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        return serializer.save(committee_id=self.request.data.get('committee'))