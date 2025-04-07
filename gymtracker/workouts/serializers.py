from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from workouts.models import Workout, Exercise


class WorkoutSerializer(ModelSerializer):
    # user = StringRelatedField() TODO
    name = serializers.CharField(
        max_length=50,
        required=True,
        error_messages={
            'required': 'Please provide the name of the workout',
            'blank': 'The name cannot be empty',
            'max_length': 'The name is too long. Maximum 50 characters.'
        }
    )

    class Meta:
        model = Workout
        fields = '__all__'


class ExerciseSerializer(ModelSerializer):
    # workout_connection = StringRelatedField() TODO
    name = serializers.CharField(
        max_length=50,
        required=True,
        error_messages={
            'required': 'Please provide the name of the exercise',
            'blank': 'The name cannot be empty',
            'max_length': 'The name is too long. Maximum 50 characters.'
        }
    )

    sets = serializers.IntegerField(
        max_value=99,
        min_value=0,
        required=True,
        error_messages={
            'required': 'Please provide number of sets',
            'blank': 'The name cannot be empty',
            'max_value': 'The number of sets cannot be more than 99',
            'min_value': 'The number of sets cannot be less than 0'
        }
    )
    reps = serializers.IntegerField(
        max_value=99,
        min_value=0,
        required=True,
        error_messages={
            'required': 'Please provide number of reps',
            'blank': 'The name cannot be empty',
            'max_value': 'The number of reps cannot be more than 99',
            'min_value': 'The number of reps cannot be less than 0'
        }
    )
    weight = serializers.FloatField(
        max_value=500,
        min_value=0,
        required=True,
        error_messages={
            'required': 'Please provide weight',
            'blank': 'The name cannot be empty',
            'max_value': 'Weight cannot be more than 500 kg',
            'min_value': 'Weight cannot be дуыы than 0'
        }
    )

    class Meta:
        model = Exercise
        fields = '__all__'
