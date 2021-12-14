from django.contrib.auth import models
from django.db.models.base import Model
from django.test import TestCase
from django.db import models

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from dentists.models import Dentist


class DentistTests(APITestCase):
    def test_create_dentist(self):
        url = reverse('add-dentist')
        data = {"name": "Dentist Fortestov", "owner": "General Kenobi", "dentists": "1", "address": "Testgatan 34A", "city": "Boras"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dentist.objects.count(), 5)
        self.assertEqual(Dentist.objects.get(id=5).name, 'Dentist Fortestov')
        self.assertEqual(Dentist.objects.get(id=5).owner, 'General Kenobi')
        self.assertEqual(Dentist.objects.get(id=5).dentists, 1)
        self.assertEqual(Dentist.objects.get(id=5).address, 'Testgatan 34A')
        self.assertEqual(Dentist.objects.get(id=5).city, 'Boras')

    def test_change_dentist_info(self):
        """
        Ensure we can change(patch) a dentist
        """
        dentist_id = 4
        url = reverse('patch-dentist', args=(dentist_id,))
        data = {"name": "Menolike Mypreviousname"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dentist.objects.get(id=4).name, 'Menolike Mypreviousname')

        def test_view_dentists(self):
            """
            Ensure we can view all dentist
            """
            url = reverse('view-dentists')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_view_dentist(self):
            """
            Ensure we can view a dentist
            """
            dentist_id = 4
            url = reverse('view-dentist', args=(dentist_id,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            

        def test_delete_dentist(self):
            """
            Ensure we can delete a dentist
            """
            dentist_id = 4
            url = reverse('delete-dentist', args=(dentist_id,))
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)