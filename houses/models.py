from django.db import models
from accounts.models import UserAccount
from buildings.models import Building, TimeStampedModel

class House(TimeStampedModel):
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="my_houses")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="building_houses")
    description = models.TextField()
    floor = models.IntegerField()
    floorCode = models.CharField(max_length=10)
    bedrooms = models.IntegerField()

class HouseAttachments(TimeStampedModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_attachments')
    file = models.FileField(upload_to=f'house/{house}/attachments/')

class HousePictures(TimeStampedModel):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="pictures")