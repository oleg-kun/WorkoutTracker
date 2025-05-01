from django.test import TestCase
from django.utils import timezone

from workouts.models import Workout
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


class WorkoutModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='test_user_1', password='testpassword')
        self.workout_1 = Workout.objects.create(
            user=self.user1,
            name='Test workout 1',
            date=timezone.make_aware(datetime(2025, 4, 13))
        )

    def test_workout_model_ok(self):
        expected_data = f'ID{self.workout_1.id}. GymDay of {self.user1.username}. Name {self.workout_1.name}. Workout was {self.workout_1.date.date()}'
        self.assertEqual(str(self.workout_1), expected_data)
