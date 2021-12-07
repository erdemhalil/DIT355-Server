# from django.db.models.fields import DateTimeField
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from appointments.models import Appointment
# from datetime import date


# class AppointmentTests(APITestCase):
#     def test_create_appointment(self):
#         """
#         Ensure we can create an appointment
#         """
#         url = reverse('create-appointment')
#         data = {'date': date.today(), 'completed': 'False', 'description': 'test description', 'dentist': 0, 'user': 0}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Appointment.objects.count(), 1)
#         self.assertEqual(Appointment.objects.get().description, 'test description')

#     def test_change_appointment(self):
#         """
#         Ensure we can change(patch) an appointment
#         """
#         appointment_id = 1
#         url = reverse('patch-appointment', args=(appointment_id,))
#         data = {"description': 'new description"}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
#         self.assertEqual(Appointment.objects.get(id=1).completed, "new description")

#     def test_view_appointments(self):
#         """
#         Ensure we can view all appointments
#         """
#         url1 = reverse('create-appointment')
#         data = {'date': date.today(), 'completed': 'False', 'description': 'test description', 'dentist': 0, 'user': 0}
#         response = self.client.post(url1, data, format='json')
#         url = reverse('view-appointments')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_view_appointment(self):
#         """
#         Ensure we can view an appointment
#         """
#         appointment_id = 0
#         url = reverse('view-appointment', args=(appointment_id,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_delete_appointment(self):
#         """
#         Ensure we can delete an appointment
#         """
#         appointment_id = 0
#         url = reverse('delete-appointment', args=(appointment_id,))
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)