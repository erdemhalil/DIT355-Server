from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializer import UserSerielizer

# Create your views here.

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

