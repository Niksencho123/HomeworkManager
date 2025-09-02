from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# TODO: Съобщенията трябва да могат да се добавят и чрез отделна страница. Засега може само от администраторския панел
class Messages(models.Model):
    messageLabel = models.CharField(max_length=255, verbose_name="Заглавие")
    messageText = models.TextField(verbose_name="Текст")
    messageImportance = models.IntegerField(verbose_name="Ниво на съобщението", validators=[MinValueValidator(-1), MaxValueValidator(1)])
    dateBegin = models.DateTimeField(verbose_name="Дата на появяне")
    dateEnd = models.DateTimeField(verbose_name="Дата на изчезване")

    def __str__(self):
        return self.messageLabel
    class Meta:
        verbose_name = "Съобщение"
        verbose_name_plural = "Съобщения"

# *Готово
class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Предмет")
    teacher = models.CharField(max_length=255, verbose_name="Учител")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    description = models.TextField(verbose_name="Описание")
    addedBy = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, verbose_name="Добавен от потребител")
    dateAdded = models.DateTimeField("Добавено на", auto_now_add=True)
    dateDue = models.DateField(verbose_name="Крайна дата")

    def __str__(self):
        return self.description
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
