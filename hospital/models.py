from django.db import models


class Hospital(models.Model):
    name = models.CharField(null=False, max_length=150)
    logo = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.EmailField(null=False, max_length=200)
    date_established = models.DateField()
    phone = models.CharField(null=False, max_length=150)

    def __str__(self):
        return f'{self.name} Hospital'
