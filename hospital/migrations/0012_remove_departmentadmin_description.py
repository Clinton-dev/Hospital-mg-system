# Generated by Django 4.1.3 on 2022-11-16 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_remove_departmentadmin_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmentadmin',
            name='description',
        ),
    ]
