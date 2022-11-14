from django.urls import path
from .views import (
    DepartmentCreateView,
    DepartmentAdminListView
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.departments, name='departments'),
    path('departments/create', DepartmentCreateView.as_view(),
         name='create-department'),
    path('departmentadmins/', DepartmentAdminListView.as_view(),
         name='department-admins'),
]
