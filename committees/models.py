from django.db import models
from buildings.models import Building


class Committee(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)