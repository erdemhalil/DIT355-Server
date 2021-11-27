from django.db import models

# Create your models here.

class Coordinate(models.Model):
    longitude = models.FloatField(default=None)
    latitude = models.FloatField(default=None)

class Openinghours(models.Model):
    monday = models.TimeField(default=None)
    tuesday = models.TimeField(default=None)
    wednesday = models.TimeField(default=None)
    thursday = models.TimeField(default=None)
    friday = models.TimeField(default=None)

class Dentist(models.Model): 
    name = models.CharField(max_length=150)
    owner = models.CharField(max_length=150)
    dentists = models.IntegerField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    coordinate = models.OneToOneField(Coordinate, on_delete=models.CASCADE, null=True)
    openinghours = models.OneToOneField(Openinghours, on_delete=models.CASCADE, null=True)

