from django.urls import path
from . import views 

urlpatterns = [
    path('list/', views.viewDentists, name='view-dentists'),
    path('detail/<str:key>/', views.viewDentist, name='view-dentist'),
    path('create/', views.addDentist, name='add-dentist'),
    path('delete/<str:key>/', views.deleteDentist, name='delete-dentist'),
    path('patch/<str:key>/', views.patchDentist, name='patch-dentist'),
]

