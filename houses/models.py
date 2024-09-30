from django.db import models
from accounts.models import UserAccount
from buildings.models import Building, TimeStampedModel

class House(TimeStampedModel):

    class StatusChoices(models.TextChoices):
        Unoccupied  = "Unoccupied", "UNOCCUPIED"
        Owner_Resided = "Owner Resided", "OWNER RESIDED"
        Rented = "Rented", "RENTED"

    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="my_houses")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="building_houses")
    description = models.TextField()
    floor = models.IntegerField()
    floorCode = models.CharField(max_length=10)
    bedrooms = models.IntegerField()
    status = models.CharField(choices=StatusChoices, default=StatusChoices.Unoccupied, max_length=50)

    class Meta:
        unique_together = ("building", "floor", "floorCode")

class HouseAttachments(TimeStampedModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_attachments')
    file = models.FileField(upload_to=f'house/{house}/attachments/')

class HousePictures(TimeStampedModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="house_pictures")
    picture = models.ImageField(upload_to=f'house/{house}/pictures/')

class Resident(TimeStampedModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="residents")
    resident = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="residences")
    isHead = models.BooleanField(default=False)
    isOwner = models.BooleanField(default=False)