from rest_framework import serializers
from .models import User

class UserSerielizer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

