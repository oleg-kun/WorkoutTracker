from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from workouts.models import Workout, Exercise


class WorkoutSerializer(ModelSerializer):
    # user = StringRelatedField() TODO

    class Meta:
        model = Workout
        fields = '__all__'


class ExerciseSerializer(ModelSerializer):
    # workout_connection = StringRelatedField() TODO
    class Meta:
        model = Exercise
        fields = '__all__'
