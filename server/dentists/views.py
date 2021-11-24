from django.shortcuts import render
from rest_framework.decorators import api_view
from  rest_framework.response import Response

from .models import Dentist
from .serializers import DentistSerializer, CoordinateSerializer

# Create your views here.

@api_view(['GET'])
def viewDentists(request):
    dentist = Dentist.objects.all()
    serializer = DentistSerializer(dentist, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewDentist(request, key):
    dentists = Dentist.objects.get(id=key)
    serializer = DentistSerializer(dentists, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addDentist(request):
    serializer = DentistSerializer(data=request.data)
    if serializer.is_valid():
        dentist = serializer.save()
        serializer = DentistSerializer(dentist)
        return Response(serializer.data)
    return Response(serializer.errors)

#update
@api_view(['POST'])
def updateDentist(request, key):
    dentist = Dentist.objects.get(id=key)
    serializer = DentistSerializer(instance=dentist, data=request.data)
    if serializer.is_valid():
        serializer.save()
    #add errorhandling 
    return Response(serializer.data) 

@api_view(['DELETE', 'GET'])
def deleteDentist(request):
    dentist = Dentist.objects.all()
    dentist.delete()
        #add errorhandling
    return Response('Dentist deleted successfully!')

