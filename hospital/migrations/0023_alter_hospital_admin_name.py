# Generated by Django 4.1.3 on 2022-11-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0022_rename_email_hospital_admin_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='admin_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]