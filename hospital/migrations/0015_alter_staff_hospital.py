# Generated by Django 4.1.3 on 2022-11-20 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital'),
        ),
    ]
