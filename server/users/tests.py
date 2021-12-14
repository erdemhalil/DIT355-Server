import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
#from rest_framework_simplejwt import
from rest_framework.test import APITestCase
from django.test import TestCase
from rest_framework.test import APIClient


class UserTestCase(APITestCase):

    def test_authenticate(self):
        data = {"email": "test@gmail.com", "first_name": "Test_name", "last_name": "test_last", "password": "password_test123"}
        self.client.post("/api/users/register/", data)
        
        data = {"email": "test@gmail.com", "password": "password_test123"}
        response = self.client.post("/api/users/token/", data)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(response.data["access"]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
