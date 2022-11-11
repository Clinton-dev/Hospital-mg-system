from django.shortcuts import render, redirect
from .forms import HospitalRegistration


def registerHospital(request):
    if request.method == "POST":
        form = HospitalRegistration(request.POST)
        if form.is_valid():
            form.save()
            print('Hospital saved')
            return redirect('/')
    else:
        form = HospitalRegistration()
    return render(request, 'hospital/register.html', {"form": HospitalRegistration})
