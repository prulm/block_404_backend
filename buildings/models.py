from django.db import models
from accounts.models import UserAccount
import houses

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

class Attachment(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    file = models.FileField(upload_to=f'building/{building}/attachments/')

class Picture(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=f"building/{building}/pictures/")

class Event(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    commences = models.DateTimeField()
    penality = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    attachment = models.FileField(upload_to=f'building/{building}/events/attachments/')

class Payment(TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    collector = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    isRecurring = models.BooleanField(default=False)
    penality = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    attachment = models.FileField(upload_to=f'building/{building}/payments/attachments/')
