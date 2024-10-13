from rest_framework import serializers
from houses.serializers import ResidentSerializer
from .models import *

class MemberSerializer(serializers.ModelSerializer):
    resident = ResidentSerializer()
    class Meta:
        model = Member
        fields = ('id', 'resident', 'position')

class MemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        exclude = ['committee']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude = ['committee']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteeAttachment
        exclude = ['committee']

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitteePicture
        exclude = ['committee']

class CommitteeSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True)
    rules = RuleSerializer(many=True)
    reports = ReportSerializer(many=True)
    committee_attachments = AttachmentSerializer(many=True)
    committee_pictures = PictureSerializer(many=True)
    class Meta:
        model = Committee
        fields = ('id', 'name', 'description', 'members', 'rules', 'reports', 'committee_attachments', 'committee_pictures')

class CreateCommitteeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Committee
        fields = '__all__'