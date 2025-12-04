from django.contrib import admin
from django.contrib.auth.models import User
from . import models

# Register your models here.
admin.site.register(models.Messages)
admin.site.register(models.Subject)
admin.site.site_header = "Официален сайт на 9.'ж' клас"
admin.site.site_title = "Администраторски панел"
admin.site.index_title = "Добре дошли в администраторския панел!"
class AssignmentAdmin(admin.ModelAdmin):
    exclude = ("addedBy",)
    def save_model(self, request, obj, form, change):
        obj.addedBy = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(models.Assignment, AssignmentAdmin)
admin.site.register(models.DutyStudent)

class ChoiceInline(admin.StackedInline):
    model = models.Choices
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question", "questionCode"]}),
        ("Начало и край", {"fields": ["beginDateTime", "endDateTime"]}),
    ]

    inlines = [ChoiceInline]

admin.site.register(models.Question, QuestionAdmin)