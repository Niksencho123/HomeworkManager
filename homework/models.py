from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
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

class AssignmentType(models.TextChoices):
    TESTWRITE = "Писмено изпитване", "Писмено изпитване"
    TESTORAL = "Устно изпитване", "Устно изпитване"
    TESTENTRY = "Входно равнище", "Входно равнище"
    TESTEXIT = "Изходно равнище", "Изходно равнище"
    HOMEWORK = "Домашна работа", "Домашна работа"
    PROJECT = "Проект", "Проект"

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    description = models.TextField(verbose_name="Описание")
    addedBy = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE, verbose_name="Добавен от потребител")
    dateAdded = models.DateTimeField("Добавено на", auto_now_add=True)
    dateDue = models.DateField(verbose_name="Крайна дата")
    typeOfAssignment = models.CharField(max_length=255, verbose_name="Тип на заданието", choices=AssignmentType.choices, default=AssignmentType.HOMEWORK)

    def __str__(self):
        return self.description
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

class DutyStudent(models.Model):
    userConn = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Потребител")
    dateBegin = models.DateField(verbose_name="Начало на дежурство")
    dateEnd = models.DateField(verbose_name="Край на дежурство")

    def __str__(self):
        begin = self.dateBegin.strftime("%d.%m.%Y") if self.dateBegin else "?"
        end = self.dateEnd.strftime("%d.%m.%Y") if self.dateEnd else "?"
        return f"Дежурство на номер {self.userConn.studentprofile.classNumber} от {begin} до {end}"
    class Meta:
        verbose_name = "Дежурство"
        verbose_name_plural = "Дежурства"