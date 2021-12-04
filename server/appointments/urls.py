from django.urls import path
from . import views 

urlpatterns = [
    path('list/', views.viewAppointments, name='view-appointments'),
    path('detail/<str:key>/', views.viewAppointment, name='view-appointment'),
    path('create/', views.addAppointment, name='create-appointment'),
    path('delete/<str:key>/', views.deleteAppointment, name='delete-appointment'),
    path('patch/<str:key>/', views.patchAppointment, name='patch-appointment')
]