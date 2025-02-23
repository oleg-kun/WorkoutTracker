from django.db import models
from django.conf import settings


# Create your models here.

class Workout(models.Model):
    # Пользователь
    # Дата тренировки
    # Название тренировки
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Это ссылка на вашу кастомную модель пользователя
        on_delete=models.CASCADE  # Указываем, что будет с этим объектом, если пользователь будет удален
    )
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)