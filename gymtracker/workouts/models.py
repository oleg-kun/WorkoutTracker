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

    def __str__(self):
        return f"This is workout of {self.name} ({self.date})"
class Exercise(models.Model):
    workout_connection = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises") #привязка к тренировке
    name = models.CharField(max_length=50)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"This is exercise {self.name}, {self.sets} x {self.reps} {self.weight}kg"

