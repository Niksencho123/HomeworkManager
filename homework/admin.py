from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Messages)
admin.site.register(models.Subject)
admin.site.register(models.Assignment)
admin.site.site_title = "Администраторски панел - 9.'ж'"
admin.site.site_header = "Административни функции"
admin.site.index_title = "Изберете един от дадени модули на сайта"