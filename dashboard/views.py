from django.shortcuts import render
from hospital.models import Department


def home(request):
    return render(request, 'dashboard/home.html')


def departments(request):
    context = {
        "departments": Department.objects.all()
    }
    return render(request, 'dashboard/departments.html', context)
