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


class DepartmentCreateView(CreateView):
    model = Department
    fields = ['name', 'description']


class DepartmentAdminListView(ListView):
    model = Department
    template_name = 'dashboard/department-admins.html'
