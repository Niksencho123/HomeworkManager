from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="Потребител", on_delete=models.CASCADE)
    profilePicture = CloudinaryField("Профилна снимка", default = "user-profile_bwwzy0")
    classNumber = models.IntegerField(default=-1, verbose_name="Номер в класа")

    def __str__(self):
        return f"Профилни данни на {self.user.username}"
    class Meta:
        verbose_name = "Профил"
        verbose_name_plural = "Профили"