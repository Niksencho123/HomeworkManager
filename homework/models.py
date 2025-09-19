from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.mail import send_mail, EmailMessage, get_connection
from django.contrib.auth.models import User
import smtplib
from email.message import EmailMessage

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
    def save(self, *args, **kwargs):
        is_new = self.pk is None 
        super().save(*args, **kwargs)
        if is_new:
            allUsers = User.objects.all()
            emails = []
            for user in allUsers:
                if user.studentprofile.sendEmails == True:
                    emails.append(user.email)
            subject = f"{self.messageLabel}"
            html_content = f"""
            <h1>Ново съобщение на сайта</h1>
            <h2>Администраторски код за важност: {self.messageImportance}</h2>
            <p style="white-space: pre-wrap;">{self.messageText}</p>
            """
            from_email = "Пощата на 9.'ж' клас <nikolaibanev123@gmail.com>"
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = from_email
            msg["To"] = ", ".join(emails)
            msg.add_alternative(html_content, subtype='html')
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login("nikolaibanev123@gmail.com", "nupj vekf ihqo djbm")
                server.send_message(msg, to_addrs=emails)

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