from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView
)
from hospital.models import Department


def home(request):
    return render(request, 'dashboard/home.html')


def departments(request):
    context = {
        "departments": Department.objects.all()
    }
    return render(request, 'dashboard/departments.html', context)


def hospital(request):
    return render(request, 'dashboard/hospital.html')


class DepartmentCreateView(CreateView):
    model = Department
    fields = ['name', 'description']


class DepartmentAdminListView(ListView):
    model = Department
    template_name = 'dashboard/department-admins.html'


class DoctorsListView(ListView):
    model = Department
    template_name = 'dashboard/doctors.html'


class ReceptionistsListView(ListView):
    model = Department
    template_name = 'dashboard/receptionists.html'


class PatientsListView(ListView):
    model = Department
    template_name = 'dashboard/patients.html'


class FoldersListView(ListView):
    model = Department
    template_name = 'dashboard/folder.html'


class FilesListView(ListView):
    model = Department
    template_name = 'dashboard/files.html'
