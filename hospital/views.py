from django.shortcuts import render, redirect
from .forms import HospitalRegistration
from django.contrib import messages
from .models import Hospital
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class HospitalCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Hospital
    form_class = HospitalRegistration
    template_name = 'hospital/register.html'
    success_url = reverse_lazy('hospital-dash')
    success_message = 'Hospital added successfully!'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


def registerHospital(request):
    form = HospitalRegistration()
    if request.method == "POST":
        form = HospitalRegistration(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.admin = request.user
            form.save()
            messages.success(request, 'Hospital added successfully!')
            return redirect('hospital-dash')

    return render(request, 'hospital/register.html', {"form": HospitalRegistration})
