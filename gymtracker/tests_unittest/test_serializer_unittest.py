from django.test import TestCase
from django.contrib.auth import get_user_model

from workouts.models import Workout, Exercise
from workouts.serializers import WorkoutSerializer, ExerciseSerializer

User = get_user_model()


class WorkoutSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='testpassword')

    def test_workout_serializer(self):
        workout_1 = Workout.objects.create(user=self.user, name='Test workout 1')
        workout_2 = Workout.objects.create(user=self.user, name='Test workout 2')
        data = WorkoutSerializer([workout_1, workout_2], many=True).data
        expected_data = [
            {
                'id': workout_1.id,
                'user': workout_1.user.id,
                'name': 'Test workout 1',
                'date': workout_1.date.isoformat().replace("+00:00", "Z")
            },
            {
                'id': workout_2.id,
                'user': workout_2.user.id,
                'name': 'Test workout 2',
                'date': workout_2.date.isoformat().replace("+00:00", "Z")
            }
        ]
        self.assertEqual(expected_data, data)


class ExerciseSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='testpassword')
        self.workout_1 = Workout.objects.create(user=self.user, name='Test workout 1')

    def test_exercise_serializer(self):
        exercise_1 = Exercise.objects.create(workout_connection=self.workout_1, name='Test exercise 1',
                                             sets=4, reps=10, weight=30.0)
        exercise_2 = Exercise.objects.create(workout_connection=self.workout_1, name='Test exercise 2',
                                             sets=4, reps=15, weight=40.0)
        data = ExerciseSerializer([exercise_1, exercise_2], many=True).data
        expected_data = [
            {
                "id": exercise_1.id,
                "name": "Test exercise 1",
                "sets": 4,
                "reps": 10,
                "weight": 30.0,
                "workout_connection": self.workout_1.id
            },
            {
                "id": exercise_2.id,
                "name": "Test exercise 2",
                "sets": 4,
                "reps": 15,
                "weight": 40.0,
                "workout_connection": self.workout_1.id
            }
        ]
        self.assertEqual(expected_data, data)