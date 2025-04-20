from django.test import TestCase
from django.contrib.auth import get_user_model

from workouts.models import Workout
from workouts.serializers import WorkoutSerializer

User = get_user_model()
class WorkoutSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='testpassword')
    def test_ok(self):
        workout_1 = Workout.objects.create(user=self.user, name='Test workout 1')
        workout_2 = Workout.objects.create(user=self.user, name='Test workout 2')
        data = WorkoutSerializer([workout_1,workout_2], many=True).data
        expected_data = [
            {
                'id':workout_1.id,
                'user':workout_1.user.id,
                'name':'Test workout 1',
                'date':workout_1.date.isoformat().replace("+00:00", "Z")
            },
            {
                'id':workout_2.id,
                'user': workout_2.user.id,
                'name': 'Test workout 2',
                'date': workout_2.date.isoformat().replace("+00:00", "Z")
            }
        ]
        self.assertEqual(expected_data, data)