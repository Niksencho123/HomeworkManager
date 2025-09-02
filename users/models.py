from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="Потребител", on_delete=models.CASCADE)
    profilePicture = models.ImageField(default='profilePictures/ordinary.png', upload_to="profilePictures", verbose_name="Потребителска снимка")
    classNumber = models.IntegerField(default=-1, verbose_name="Номер в класа")

    def __str__(self):
        return f"Профилни данни на {self.user.username}"
    class Meta:
        verbose_name = "Профил"
        verbose_name_plural = "Профили"