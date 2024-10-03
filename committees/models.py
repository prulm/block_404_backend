from django.db import models
from accounts.models import UserAccount
from buildings.models import Building, TimeStampedModel


class Committee(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

class Members(TimeStampedModel):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, default="Member")