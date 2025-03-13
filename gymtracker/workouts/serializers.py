from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from workouts.models import Workout, Exercise


class WorkoutSerializer(ModelSerializer):
    user = StringRelatedField()

    class Meta:
        model = Workout
        fields = ['user', 'date', 'name']


class ExerciseSerializer(ModelSerializer):
    workout_connection = StringRelatedField()

    class Meta:
        model = Exercise
        fields = ['workout_connection', 'name', 'sets', 'reps', 'weight']
