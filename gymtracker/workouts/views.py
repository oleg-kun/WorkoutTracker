from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from workouts.models import Workout, Exercise
from workouts.serializers import WorkoutSerializer, ExerciseSerializer


def all_workouts_view(request):
    pass

class WorkoutView(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class ExerciseView(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
