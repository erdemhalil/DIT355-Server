from django.urls import path
from . import views 

urlpatterns = [
    path('appointment-list/', views.viewAppointments, name='view-appointments'),
    path('appointment-detail/<str:key>/', views.viewAppointment, name='view-appointment'),
    path('appointment-create/', views.addAppointment, name='create-appointment'),
    path('appointment-delete/<str:key>/', views.deleteAppointment, name='delete-appointment')
]