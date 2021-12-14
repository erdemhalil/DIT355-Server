from django.urls import path
from django.urls import include, path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.saveUser, name='register_users'),
    path('edit/', views.editUser, name='edit_users'),
    path('list/', views.viewUsers, name='view_users'),
    path('detail/<str:key>/', views.viewUser, name='view_user'),
    path('delete/<str:key>/', views.deleteUser, name='delete_user'),
]


