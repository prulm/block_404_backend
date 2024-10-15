from django.db import IntegrityError
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
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
    
    def create(self, request, *args, **kwargs):
         try:
             return super().create(request, *args, **kwargs)
         except IntegrityError as err:
             if 'unique constraint' in str(err):
                return Response(
                    {'Error': 'Each member should be unique to a committee.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
             else:
                raise IntegrityError(err)

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