from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from gymtracker.permissions import UserOnlyPermission
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
    permission_classes = [UserOnlyPermission]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user.id == request.user.id:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({"detail": "У вас нет доступа к этой тренировке."}, status=403)

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


class ExerciseView(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'workout_connection__name']
    ordering_fields = ['name', 'weight']
    permission_classes = [UserOnlyPermission]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.workout_connection.user.id == request.user.id:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({"detail": "У вас нет доступа к этому упражнению."}, status=403)

    def get_queryset(self):
        return Exercise.objects.filter(workout_connection__user=self.request.user)
