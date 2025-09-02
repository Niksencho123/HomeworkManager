from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    userConn = models.ForeignKey(User, verbose_name="Потребител", on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Съобщение")
    dateAdded = models.DateTimeField(verbose_name="Дата на добавяне", auto_now_add=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Постове"