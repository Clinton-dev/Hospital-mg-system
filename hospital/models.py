from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Hospital(models.Model):
    name = models.CharField(null=False, max_length=150)
    logo = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.EmailField(null=False, max_length=200)
    date_established = models.DateField()
    phone = models.CharField(null=False, max_length=150)
    admin = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} Hospital'


class Department(models.Model):
    name = models.CharField(null=True, max_length=150)
    date_created = models.DateTimeField(null=True, default=timezone.now)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    # department_admin = models.ForeignKey(
    #     User, on_delete=models.DO_NOTHING, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.name} Department'


class DepartmentAdmin(models.Model):
    depadmin = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.depadmin.username} {self.department.name} Department admin'


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    role = models.TextField(max_length=70, default=True)
    image = models.ImageField(default='default.svg', upload_to='profile_pics')
    department = models.ForeignKey(
        Department, null=True, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(null=True, default=timezone.now)

    def __str__(self):
        return f'{self.user.username} staff profile'


class SubDepartment(models.Model):
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} subdepartment'


class Patient(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    national_id = models.CharField(max_length=25)
    date_created = models.DateTimeField(null=False, default=timezone.now)
    hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} patient'


class Folder(models.Model):
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.name} Folder'


class File(models.Model):
    #fields = ['name','file','folder',]
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to='file-uploads/%Y/%m/%D/', max_length=254)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self) -> str:
        return f'{self.name} File'
