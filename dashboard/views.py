import http
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView
)
from django.contrib.auth.decorators import login_required
from hospital.models import Department, File, Folder, DepartmentAdmin, Patient, Staff
from django.contrib.auth.mixins import LoginRequiredMixin  # Restrict user access
from django.contrib.messages.views import SuccessMessageMixin  # display flash message
from django.urls import reverse_lazy
from django.db.models import Q
from .utils import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import Group


def search_patients(request):
    if request.method == "GET":
        query = request.GET.get('query')

        if query != None:
            lookup = (Q(first_name__icontains=query)
                      | Q(last_name__icontains=query)
                      | Q(national_id__icontains=query))
            patients = Patient.objects.filter(lookup)
            return render(request, 'dashboard/search.html', {'patients': patients})
    return render(request, 'dashboard/search.html', {})


@ login_required(login_url='users/login_user')
def home(request):
    context = {
        'is_admin': is_hospital_admin(request.user),
        'is_depadmin': is_department_admin(request.user),
        'is_staff': is_hospital_staff(request.user),
    }
    return render(request, 'dashboard/home.html', context)


@ login_required(login_url='users/login_user')
def departments(request):
    print(request.user.hospital)
    context = {
        "departments": Department.objects.all()
    }
    return render(request, 'dashboard/departments.html', context)


@ login_required(login_url='users/login_user')
def hospital(request):
    return render(request, 'dashboard/hospital.html')

# Department section


class DepartmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Department
    fields = ['name', 'description']
    success_url = reverse_lazy('departments')
    success_message = 'Department created successfully!'

    def form_valid(self, form):
        form.instance.hospital = self.request.user.hospital
        return super().form_valid(form)


class DepartmentsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Department
    fields = ['name', 'description']
    success_url = reverse_lazy('departments')
    success_message = 'Department updated successfully!'

    def form_valid(self, form):
        form.instance.hospital = self.request.user.hospital
        return super().form_valid(form)


class DepartmentsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('departments')
    success_message = 'Department deleted successfully!'


# Department Admin section


class DepartmentAdminListView(ListView):
    model = DepartmentAdmin
    template_name = 'dashboard/department-admins.html'
    context_object_name = 'departmentadmins'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentAdminListView,
                        self).get_context_data(*args, **kwargs)
        context['is_admin'] = is_hospital_admin(self.request.user)
        context['is_depadmin'] = is_hospital_admin(self.request.user)
        return context


class DepartmentAdminsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = DepartmentAdmin
    fields = "__all__"
    success_url = reverse_lazy('department-admins')
    success_message = 'Department created successfully!'


class DepartmentAdminsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = DepartmentAdmin
    fields = "__all__"
    success_url = reverse_lazy('department-admins')
    success_message = 'Department updated successfully!'


class DepartmentAdminsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = DepartmentAdmin
    success_url = reverse_lazy('department-admins')
    success_message = 'Department admin deleted successfully!'

# Doctors section


class DoctorsListView(ListView):
    model = Department
    template_name = 'dashboard/doctors.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(DoctorsListView,
                        self).get_context_data(*args, **kwargs)
        context['is_admin'] = is_hospital_admin(self.request.user)
        context['is_depadmin'] = is_hospital_admin(self.request.user)
        return context


class DoctorsCreateView(CreateView):
    model = User
    template_name = 'hospital/doctor_form.html'
    fields = ['username', 'email', 'last_name', 'first_name']

    def get_context_data(self, *args, **kwargs):
        context = super(DoctorsCreateView,
                        self).get_context_data(*args, **kwargs)
        context['is_depadmin'] = is_department_admin(self.request.user)
        context['is_admin'] = is_hospital_admin(self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        print(request)
        if form.is_valid():
            user = form.save()
            # create random password
            randpass = User.objects.make_random_password()
            user.set_password(randpass)
            user.save()
            # associate user with staff group
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            username = form.cleaned_data.get('username')

            # link staff model link wth user and hospital
            staff_prof = Staff.objects.create(
                user=user, hospital=self.request.user.hospital)
            staff_prof.save()
            # send email with login details
            # redirect to doctors list page
            messages.success(
                request, f'User with username: {username} was created with following password: {randpass}')
            return redirect('doctors')

        return render(request, self.template_name, {'form': form})

# Receptionist section


class ReceptionistsListView(ListView):
    model = Department
    template_name = 'dashboard/receptionists.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ReceptionistsListView,
                        self).get_context_data(*args, **kwargs)
        context['is_admin'] = is_hospital_admin(self.request.user)
        context['is_depadmin'] = is_hospital_admin(self.request.user)
        return context


class ReceptionistsCreateView(CreateView):
    model = User
    template_name = 'hospital/receptionist_form.html'
    fields = ['username', 'email', 'last_name', 'first_name']

    def get_context_data(self, *args, **kwargs):
        context = super(ReceptionistsCreateView,
                        self).get_context_data(*args, **kwargs)
        context['is_depadmin'] = is_department_admin(self.request.user)
        context['is_admin'] = is_hospital_admin(self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        print(request)
        if form.is_valid():
            user = form.save()
            randpass = User.objects.make_random_password()
            user.set_password(randpass)
            user.save()
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            staff_prof = Staff.objects.create(
                user=user, hospital=self.request.user.hospital)
            staff_prof.save()
            # send email with login details
            messages.success(
                request, f'User with username: {username} was created with following password: {randpass}')
            return redirect('receptionists')

        return render(request, self.template_name, {'form': form})


# Patients section

class PatientsListView(ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'dashboard/patients.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PatientsListView,
                        self).get_context_data(*args, **kwargs)
        context['is_admin'] = is_hospital_admin(self.request.user)
        context['is_depadmin'] = is_hospital_admin(self.request.user)
        return context


class PatientsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy('patients')
    success_message = 'Patient created successfully!'


class PatientsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy('patients')
    success_message = 'Patient updated successfully!'


class PatientsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('patients')
    success_message = 'Patient deleted successfully!'

# Folders section


class FoldersListView(ListView):
    model = Folder
    template_name = 'dashboard/folder.html'
    context_object_name = 'folders'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(FoldersListView,
                        self).get_context_data(*args, **kwargs)
        context['is_admin'] = is_hospital_admin(self.request.user)
        context['is_depadmin'] = is_hospital_admin(self.request.user)
        return context


class FoldersCreateView(SuccessMessageMixin, CreateView):
    model = Folder
    fields = ['name', 'department']
    success_url = reverse_lazy('folders')
    success_message = 'folder created successfully!'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class FoldersUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Folder
    fields = ['name', 'department']
    success_url = reverse_lazy('folders')
    success_message = 'folder updated successfully!'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class FoldersDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Folder
    success_url = reverse_lazy('folders')
    success_message = 'folder deleted successfully!'

# Files sections


class FilesListView(ListView):
    model = File
    template_name = 'dashboard/files.html'
    context_object_name = 'files'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(FilesListView,
                        self).get_context_data(*args, **kwargs)
        context['is_admin'] = is_hospital_admin(self.request.user)
        context['is_depadmin'] = is_hospital_admin(self.request.user)
        return context


class FilesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = File
    fields = ['name', 'file', 'folder']
    success_url = reverse_lazy('files')
    success_message = 'file created successfully!'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class FilesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = File
    fields = ['name', 'file', 'folder']
    success_url = reverse_lazy('files')
    success_message = 'file updated successfully!'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super().form_valid(form)


class FilesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = File
    success_url = reverse_lazy('files')
    success_message = 'File deleted successfully!'
