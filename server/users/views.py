from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializer import UserSerielizer, UserSaveSerializer

# Create your views here.

@api_view(['POST'])
def saveUser(request):
    serializer = UserSaveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def editUser(request):
    user = User.objects.get(email=request.user)  
    serializer = UserSerielizer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def viewUsers(request):
    users = User.objects.all()
    serializer = UserSerielizer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewUser(request, key):
    try:
        user = User.objects.get(id=key)
        serializer = UserSerielizer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response('User not found.', status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteUser(request, key):
    try:
        user = User.objects.get(id=key)
        user.delete()
        return Response('User deleted succsesfully!')
    except User.DoesNotExist:
        return Response('User does not exist.', status=status.HTTP_404_NOT_FOUND)

