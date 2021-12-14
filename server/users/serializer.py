from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerielizer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class UserSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], password=make_password(validated_data['password']))
        return user

