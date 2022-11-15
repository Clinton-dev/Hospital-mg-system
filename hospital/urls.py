from django.urls import path
from .views import HospitalCreateView
from . import views

urlpatterns = [
    # path('', views.registerHospital, name='register-hospital-view'),
    path('', HospitalCreateView.as_view(), name='register-hospital')
]
