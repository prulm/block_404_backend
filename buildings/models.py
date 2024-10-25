from django.db import models
from location_field.models.plain import PlainLocationField

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
    location = PlainLocationField(zoom=18)

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
    reason = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=10)
