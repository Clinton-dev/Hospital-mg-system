from django.urls import path
from .views import HospitalCreateView, HospitalDeleteView
from . import views

urlpatterns = [
    # path('', views.registerHospital, name='register-hospital-view'),
    path('', HospitalCreateView.as_view(), name='register-hospital'),
    path('delete/<int:pk>/', HospitalDeleteView.as_view(), name='delete-hospital')
]
