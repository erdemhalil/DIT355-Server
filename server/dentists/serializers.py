from rest_framework import fields, serializers

from .models import Coordinate, Dentist, Openinghours

class CoordinateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Coordinate
        fields =  '__all__'

class OpeninghoursSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Openinghours
        fields = '__all__'

class DentistSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Dentist
        fields = '__all__'

