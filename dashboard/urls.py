from django.urls import path
from .views import (
    DepartmentCreateView,
    DepartmentAdminListView,
    DoctorsListView,
    FilesListView,
    FoldersListView,
    PatientsListView,
    ReceptionistsListView
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hospital-dash/', views.hospital, name='hospital-dash'),
    path('departments/', views.departments, name='departments'),
    path('departments/create', DepartmentCreateView.as_view(),
         name='create-department'),
    path('departmentadmins/', DepartmentAdminListView.as_view(),
         name='department-admins'),
    path('doctors/', DoctorsListView.as_view(),
         name='doctors'),
    path('receptionists/', ReceptionistsListView.as_view(),
         name='receptionists'),
    path('folders/', FoldersListView.as_view(),
         name='folders'),
    path('files/', FilesListView.as_view(),
         name='files'),
    path('patients/', PatientsListView.as_view(),
         name='patients'),
]
