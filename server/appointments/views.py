from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from appointments.models import Appointment
from appointments.serializer import AppointmentSerializer

# Create your views here.

@api_view(['GET'])
def viewAppointments(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewAppointment(request, key):
    try:
        appointment = Appointment.objects.get(id=key)
        serializer  = AppointmentSerializer(appointment, many=False).data
        return Response(serializer)
    except Appointment.DoesNotExist:
        return Response('Appointment does not exist', status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addAppointment(request):
    try:
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            appointment = serializer.save()
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    except Exception as e:
        return Response('Something went wrong ' + e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def patchAppointment(request, key):
    appointment = Appointment.objects.get(id=key)
    serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteAppointment(request, key):
    try:
        appointment = Appointment.objects.get(id=key)
        appointment.delete()
        return Response('Appointment deleted successfully!', status=status.HTTP_200_OK)
    except Appointment.DoesNotExist:
        return Response('Appointment does not exist.', status=status.HTTP_404_NOT_FOUND)

    