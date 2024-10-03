from django.db import models
from accounts.models import UserAccount
from buildings.models import Building, TimeStampedModel


class Committee(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

class Member(TimeStampedModel):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, default="Member")

class Rule(TimeStampedModel):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name="rules")
    rule = models.TextField()
    order = models.IntegerField()
    picture = models.ImageField(upload_to=f"committees/{committee.name}/rules/pictures/")

class Report(TimeStampedModel):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name="reports")
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to=f"committees/{committee.name}/reports/")

class CommitteeAttachments(TimeStampedModel):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name="committee_attachments")
    file = models.FileField(upload_to=f"committees/{committee.name}/attachments/")
    description = models.TextField(blank=True, null=True)

class CommitteePictures(TimeStampedModel):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name="committee_pictures")
    picture = models.ImageField(upload_to=f"committees/{committee.name}/pictures/")
    description = models.TextField(blank=True, null=True)
    