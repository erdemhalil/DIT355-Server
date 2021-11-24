from django.urls import path
from . import views 

urlpatterns = [
    path('dentist-list/', views.viewDentists, name='view-dentists'),
    path('dentist-detail/<str:key>/', views.viewDentist, name='view-dentist'),
    path('dentist-create/', views.addDentist, name='add-dentist'),
    path('dentist-update/<str:key>/', views.updateDentist, name='update-dentist'),
    path('dentist-delete/', views.deleteDentist, name='delete-dentist'),
]

