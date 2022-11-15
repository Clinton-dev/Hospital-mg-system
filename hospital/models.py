from django.db import models
from django.contrib.auth.models import User


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
    description = models.TextField(blank=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} Department'


class SubDepartment(models.Model):
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} subdepartment'


class Folder(models.Model):
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.name} Folder'
