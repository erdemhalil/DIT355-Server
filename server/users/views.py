from django.shortcuts import render
from rest_framework.decorators import api_view
from  rest_framework.response import Response

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
    user = User.objects.get(id=key)
    serializer = UserSerielizer(user, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request, key):
    user = User.objects.get(id=key)
    user.delete()
        #add errorhandling 
    return Response('User deleted succsesfully!')

