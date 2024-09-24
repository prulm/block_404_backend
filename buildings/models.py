from django.db import models

class Building(models.Model):
    name = models.CharField(unique=True)
    description = models.TextField(blank=True, null=True)
    houses = models.IntegerField()
    floors = models.IntegerField()
    address = models.CharField(max_length=255)

class Attachment(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')