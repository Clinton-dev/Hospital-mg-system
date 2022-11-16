from django.contrib import admin
from . import models

admin.site.register(models.Hospital)
admin.site.register(models.Department)
admin.site.register(models.Folder)
admin.site.register(models.File)
