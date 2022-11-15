from django.shortcuts import render, redirect
from .forms import HospitalRegistration
from django.contrib import messages


def registerHospital(request):
    if request.method == "POST":
        form = HospitalRegistration(request.POST)
        if form.is_valid():
            form.save()
            print('Hospital saved')
            messages.success(request, 'Hospital added successfully!')
            return redirect('/')
    else:
        form = HospitalRegistration()
    return render(request, 'hospital/register.html', {"form": HospitalRegistration})
