from django.db import models
from datetime import datetime
from accounts.models import UserAccount

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Building(TimeStampedModel):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    housesPerFloor = models.IntegerField()
    floors = models.IntegerField()
    address = models.CharField(max_length=255)

    @property
    def houses(self):
        return self.housesPerFloor * self.floors

class BuildingAttachment(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to=f'building/{building.name}/attachments/')

class BuildingPicture(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='pictures')
    picture = models.ImageField(upload_to=f"building/{building.name}/pictures/")

class Penality(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='penalities')
    reason = models.TextField()
    amount = models.IntegerField()

class Event(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='events')
    creator = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    commences = models.DateTimeField()
    penality = models.ForeignKey(Penality, on_delete=models.CASCADE, null=True, blank=True)
    attachment = models.FileField(upload_to=f'building/{building.name}/events/attachments/')

class Payment(TimeStampedModel):

    class PaymentTypes(models.TextChoices):
        Power = 'Power', 'POWER'
        Water = 'Water', 'WATER'
        Other = 'Other', 'OTHER'

    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='payments')
    collector = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=PaymentTypes.choices, default=PaymentTypes.Other)
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    isRecurring = models.BooleanField(default=False)
    recurrence_period = models.IntegerField(null=True, blank=True)
    penality = models.ForeignKey(Penality, on_delete=models.CASCADE, null=True, blank=True)
    attachment = models.FileField(upload_to=f'building/{building.name}/payments/attachments/', null=True, blank=True)
