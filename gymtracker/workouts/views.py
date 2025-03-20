from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from workouts.models import Workout, Exercise
from workouts.serializers import WorkoutSerializer, ExerciseSerializer


def authentication_github(request):
    return render(request, 'oauth.html')


class WorkoutView(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'user']
    ordering_fields = ['name', 'date']
    # permission_classes = [IsAuthenticated]


class ExerciseView(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'workout_connection__name']
    ordering_fields = ['name', 'weight']
    # permission_classes = [IsAuthenticated]
