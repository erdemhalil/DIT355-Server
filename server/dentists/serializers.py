from types import coroutine
from rest_framework import serializers

from .models import Dentist, Coordinate

class CoordinateSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Coordinate
        fields = '__all__'


class DentistSerializer(serializers.ModelSerializer): 
    coordinate = {}
    class Meta: 
        model = Dentist
        fields = '__all__'

