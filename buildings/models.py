from django.db import models
import houses

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Building(TimeStampedModel):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    houses = models.IntegerField()
    floors = models.IntegerField()
    address = models.CharField(max_length=255)

    @property
    def houses(self):
        pass

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
    penality = models.DecimalField(max_digits=10, decimal_places=2)
    commences = models.DateTimeField()
    attachment = models.FileField(upload_to=f'building/{building}/events/attachments/')

