# Generated by Django 4.1.3 on 2022-11-27 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0025_alter_staff_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(blank=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hospital.department'),
        ),
    ]
