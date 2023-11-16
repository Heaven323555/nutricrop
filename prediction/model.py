# models.py
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)

class Yield(models.Model):
    district = models.CharField(max_length=100)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    area = models.FloatField()
