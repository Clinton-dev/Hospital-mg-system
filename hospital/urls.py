from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerHospital, name='register-hospital'),
]
