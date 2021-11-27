from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Dentist, Coordinate, Openinghours
from .serializers import DentistSerializer, CoordinateSerializer, OpeninghoursSerializer

# Create your views here.

@api_view(['GET'])
def viewDentists(request):
    dentists = Dentist.objects.all()
    serializer = DentistSerializer(dentists, many=True)
    for i in serializer.data:
        key = i.pop('coordinate')
        coordinates = Coordinate.objects.get(id=key)
        coordinate = CoordinateSerializer(coordinates, many=False)
        result = coordinate.data
        result.pop('id')
        i['coordinate'] = result
    for i in serializer.data:
        key = i.pop('openinghours')
        openinghour = Openinghours.objects.get(id=key)
        openinghours = OpeninghoursSerializer(openinghour, many=False)
        result = openinghours.data
        result.pop('id')
        i['openinghours'] = result
    return Response(serializer.data)

@api_view(['GET'])
def viewDentist(request, key):
    try:
        dentist = Dentist.objects.get(id=key)
        serializer = DentistSerializer(dentist, many=False).data
        cKey = serializer.pop('coordinate')
        coordinates = Coordinate.objects.get(id=cKey)
        coordinate = CoordinateSerializer(coordinates, many=False).data
        coordinate.pop('id')
        serializer['coordinate'] = coordinate
        oKey = serializer.pop('openinghours')
        openinghour = Openinghours.objects.get(id=oKey)
        openinghours = OpeninghoursSerializer(openinghour, many=False).data
        serializer['openinghours'] = openinghours
        return Response(serializer)
    except Dentist.DoesNotExist:
        return Response('Exception: Dentist Not Found', status=status.HTTP_404_NOT_FOUND)
    except Coordinate.DoesNotExist:
        return Response('Exception: Coordinate Not Found', status=status.HTTP_404_NOT_FOUND)
    except Openinghours.DoesNotExist:
        return Response('Exception: Opening Hours Not Found', status=status.HTTP_404_NOT_FOUND)
    except:
        return Response('Something went wrong.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def addDentist(request):
    try:
        if 'coordinate' in request.data:
            coordinates = request.data.pop('coordinate')
            coordinate = addCoordinate(coordinates)
            request.data['coordinate'] = coordinate
        if 'openinghours' in request.data:
            openings = request.data.pop('openinghours')
            openinghours = addOpenings(openings)
            request.data['openinghours'] = openinghours
        serializer = DentistSerializer(data=request.data)
        if serializer.is_valid():
            dentist = serializer.save()
            serializer = DentistSerializer(dentist)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    except Exception as e:
        return Response('Something went wrong ' + e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def deleteDentist(request, key):
    try:
        dentist = Dentist.objects.get(id=key)
        dentist.delete()
        return Response('Dentist deleted successfully!', status=status.HTTP_200_OK)
    except Dentist.DoesNotExist:
        return Response('Dentist does not exist', status=status.HTTP_404_NOT_FOUND)

def addCoordinate(request):
    serializer = CoordinateSerializer(data=request)
    if serializer.is_valid():
        coordinate = serializer.save()
        serializer = CoordinateSerializer(coordinate)
        return serializer.data.get('id')
    return serializer.errors

def addOpenings(request):
    serializer = OpeninghoursSerializer(data=request)
    if serializer.is_valid():
        opennings = serializer.save()
        serializer = OpeninghoursSerializer(opennings)
        return serializer.data.get('id')
    return serializer.errors
