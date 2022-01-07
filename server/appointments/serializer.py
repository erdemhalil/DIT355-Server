from rest_framework import serializers
from .models import Appointment
from dentists.serializers import DentistSerializer

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentReadSerializer(serializers.ModelSerializer):
    dentist = DentistSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'