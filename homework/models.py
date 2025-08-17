from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# TODO: Съобщенията трябва да могат да се добавят и чрез отделна страница
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

