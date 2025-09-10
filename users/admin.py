from django.contrib import admin
from . import models

# Register your models here.
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "classNumber"]
admin.site.register(models.StudentProfile, StudentProfileAdmin)