from django.db import models

# Create your models here.

class Coordinate(models.Model):
    longitude = models.FloatField(blank=True)
    latitude = models.FloatField(blank=True)

class Openinghours(models.Model):
    monday = models.CharField(blank=True, max_length=150)
    tuesday = models.CharField(blank=True, max_length=150)
    wednesday = models.CharField(blank=True, max_length=150)
    thursday = models.CharField(blank=True, max_length=150)
    friday = models.CharField(blank=True, max_length=150)
    timestaken = models.CharField(blank=True, null=True, default=None, max_length=150)

class Dentist(models.Model): 
    name = models.CharField(max_length=150)
    owner = models.CharField(max_length=150)
    dentists = models.IntegerField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    coordinate = models.OneToOneField(Coordinate, on_delete=models.CASCADE, null=True)
    openinghours = models.OneToOneField(Openinghours, on_delete=models.CASCADE, null=True)

