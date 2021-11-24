from django.db import models

# Create your models here.

class Dentist(models.Model): 
    name = models.CharField(max_length=150, unique=True)
    owner = models.CharField(max_length=150)
    dentists = models.IntegerField()
    address = models.CharField(max_length=150, unique=True)
    city = models.CharField(max_length=150)


class Coordinate(models.Model):
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    longitude = models.FloatField(unique=True)
    latitude = models.FloatField(unique=True)


class Openinghours(models.Model):
    monday = models.TimeField()
    tuesday = models.TimeField()
    wednesday = models.TimeField()
    thursday = models.TimeField()
    friday = models.TimeField()