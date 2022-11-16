from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView
)
from django.contrib.auth.decorators import login_required
from hospital.models import Department, File, Folder
from django.contrib.auth.mixins import LoginRequiredMixin  # Restrict user access
from django.contrib.messages.views import SuccessMessageMixin  # display flash message
from django.urls import reverse_lazy


@login_required(login_url='users/login_user')
def home(request):
    return render(request, 'dashboard/home.html')


@login_required(login_url='users/login_user')
def departments(request):
    print(request.user.hospital)
    context = {
        "departments": Department.objects.all()
    }
    return render(request, 'dashboard/departments.html', context)


@login_required(login_url='users/login_user')
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
    model = Department
    template_name = 'dashboard/department-admins.html'

# Doctors section


class DoctorsListView(ListView):
    model = Department
    template_name = 'dashboard/doctors.html'


class ReceptionistsListView(ListView):
    model = Department
    template_name = 'dashboard/receptionists.html'


class PatientsListView(ListView):
    model = Department
    template_name = 'dashboard/patients.html'

# Folders section


class FoldersListView(ListView):
    model = Folder
    template_name = 'dashboard/folder.html'
    context_object_name = 'folders'
    # ordering = ['created_at']


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
