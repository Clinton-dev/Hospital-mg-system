from django.urls import path
from .views import (
    DepartmentAdminsCreateView,
    DepartmentAdminsDeleteView,
    DepartmentAdminsUpdateView,
    DepartmentCreateView,
    DepartmentsDeleteView,
    DepartmentsUpdateView,
    DepartmentAdminListView,
    DoctorsListView,
    FilesListView,
    FilesCreateView,
    FilesUpdateView,
    FilesDeleteView,
    FoldersListView,
    FoldersDeleteView,
    FoldersUpdateView,
    PatientsListView,
    ReceptionistsListView,
    FoldersCreateView
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hospital-dash/', views.hospital, name='hospital-dash'),
    path('departments/', views.departments, name='departments'),
    path('departments/create', DepartmentCreateView.as_view(),
         name='create-department'),
    path('departments/<int:pk>/update', DepartmentsUpdateView.as_view(),
         name='deparment-update'),
    path('departments/<int:pk>/delete', DepartmentsDeleteView.as_view(),
         name='department-delete'),
    path('departmentadmins/', DepartmentAdminListView.as_view(),
         name='department-admins'),
    path('departmentadmins/create/', DepartmentAdminsCreateView.as_view(),
         name='departmentadmins-create'),
    path('departmentadmins/<int:pk>/update', DepartmentAdminsUpdateView.as_view(),
         name='departmentadmins-update'),
    path('departmentadmins/<int:pk>/delete', DepartmentAdminsDeleteView.as_view(),
         name='departmentadmins-delete'),
    path('doctors/', DoctorsListView.as_view(),
         name='doctors'),
    path('receptionists/', ReceptionistsListView.as_view(),
         name='receptionists'),
    path('folders/', FoldersListView.as_view(),
         name='folders'),
    path('folders/create/', FoldersCreateView.as_view(),
         name='folders-create'),
    path('folders/<int:pk>/update', FoldersUpdateView.as_view(),
         name='folder-update'),
    path('folders/<int:pk>/delete', FoldersDeleteView.as_view(),
         name='folder-delete'),
    path('files/', FilesListView.as_view(),
         name='files'),
    path('files/create/', FilesCreateView.as_view(),
         name='files-create'),
    path('files/<int:pk>/update', FilesUpdateView.as_view(),
         name='file-update'),
    path('files/<int:pk>/delete', FilesDeleteView.as_view(),
         name='file-delete'),
    path('patients/', PatientsListView.as_view(),
         name='patients'),
]
