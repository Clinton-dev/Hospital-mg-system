from django.shortcuts import render, redirect
from .forms import HospitalRegistration
from django.contrib import messages
from .models import Hospital, Staff
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail


class HospitalCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Hospital
    form_class = HospitalRegistration
    template_name = 'hospital/register.html'
    success_url = reverse_lazy('owner')
    success_message = 'Hospital added successfully!'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('admin_name')
            namelist = name.split()
            username = namelist[0]+namelist[1]
            phone = form.cleaned_data.get('admin_phone')
            email = form.cleaned_data.get('admin_email')
            randPass = User.objects.make_random_password()
            hospital_admin = User.objects.create_user(
                username=username, password=randPass, email=email)
            print('usercreated!')
            group = Group.objects.get(name='admin')
            hospital_admin.groups.add(group)
            admin_prof = Staff.objects.create(
                user=hospital_admin, hospital=form.instance, role='admin')
            admin_prof.save()
            send_mail(
                subject='Admin Login credentials',
                message=f'Use the following credentials to login username: {username}  password: {randPass} ',
                recipient_list=[hospital_admin.email],
                from_email=None,
                fail_silently=False,
            )
            hospital_name = form.cleaned_data.get('name')

            # redirect to doctors list page
            messages.success(
                request, f'Hospital {hospital_name} was created with: {username} as admin')
            return redirect('owner')

        return render(request, self.template_name, {'form': form})


class HospitalDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Hospital
    success_url = reverse_lazy('owner')
    success_message = 'hospital deleted successfully!'


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
