# Generated by Django 4.1.3 on 2022-11-16 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_departmentadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmentadmin',
            name='name',
        ),
    ]
