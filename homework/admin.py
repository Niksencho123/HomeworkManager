from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Messages)
admin.site.register(models.Subject)
admin.site.site_title = "Администраторски панел - 9.'ж'"
admin.site.site_header = "Административни функции"
admin.site.index_title = "Изберете един от дадени модули на сайта"

class AssignmentAdmin(admin.ModelAdmin):
    exclude = ("addedBy",)
    def save_model(self, request, obj, form, change):
        obj.addedBy = request.user
        return super().save_model(request, obj, form, change)
admin.site.register(models.Assignment, AssignmentAdmin)