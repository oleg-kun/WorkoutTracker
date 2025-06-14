import json
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from dotenv import load_dotenv
import os

from workouts.models import Workout, Exercise
from workouts.serializers import WorkoutSerializer, ExerciseSerializer

User = get_user_model()


class WorkoutApiTestCase(APITestCase):
    def setUp(self):
        load_dotenv("C:/Users/User/PycharmProjects/projectWorckoutTracker/gymtracker/.env")
        load_dotenv("C:/Users/User/PycharmProjects/projectWorckoutTracker/gymtracker/.env.local")
        self.user1 = User.objects.create_user(username='test_user_1', password='testpassword')
        self.user2 = User.objects.create_user(username='test_user_2', password='testpassword')
        self.client.login(username='test_user_1', password='testpassword')

    def test_get(self):
        workout_1 = Workout.objects.create(user=self.user1, name='Test workout 1')
        workout_2 = Workout.objects.create(user=self.user1, name='Test workout 2')
        url = reverse('workout-list')
        responce = self.client.get(url)
        serializer_data = WorkoutSerializer([workout_1, workout_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, responce.status_code)
        self.assertEqual(serializer_data, responce.data)

    def test_get_filter(self):
        workout_1 = Workout.objects.create(user=self.user2, name='Test workout 1 by test_user_1')
        workout_2 = Workout.objects.create(user=self.user1, name='Test workout 2')
        workout_3 = Workout.objects.create(user=self.user1, name='Test workout 1')  # filter workout name
        workout_4 = Workout.objects.create(user=self.user1, name='Test workout 1')  # filter workout name
        url = reverse('workout-list')
        responce = self.client.get(url, data={'name': 'Test workout 1'})
        serializer_data = WorkoutSerializer([workout_3, workout_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, responce.status_code)
        self.assertEqual(serializer_data, responce.data)

    def test_get_search(self):
        workout_1 = Workout.objects.create(user=self.user1, name='Test workout 1 FIND_ME_TEXT')  # search workout name
        workout_2 = Workout.objects.create(user=self.user1, name='Test workout 2 FIND_ME_TEXT')
        workout_3 = Workout.objects.create(user=self.user1, name='Test workout 3')
        url = reverse('workout-list')
        responce = self.client.get(url, data={'search': 'FIND_ME_TEXT'})
        serializer_data = WorkoutSerializer([workout_1, workout_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, responce.status_code)
        self.assertEqual(serializer_data, responce.data)

    def test_get_id(self):
        workout_1 = Workout.objects.create(user=self.user1, name='Test workout 1')
        url = reverse('workout-detail', args=[workout_1.id])
        responce = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, responce.status_code)
        self.assertEqual(workout_1.id, responce.data['id'] )
        self.assertEqual(workout_1.name, responce.data['name'])

    def test_create(self):
        url = reverse('workout-list')
        data = {
            "name": "Test workout Unittest",
            "user": self.user1.id
        }
        json_data = json.dumps(data)
        responce = self.client.post(url, data=json_data,
                                    content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, responce.status_code)
        self.assertEqual(1, Workout.objects.all().count())

    def test_update(self):
        workout_1 = Workout.objects.create(user=self.user1, name='Test workout 1')
        url = reverse('workout-detail', args=(workout_1.id,))
        data = {
            "name": "Test workout Unittest",
            "user": self.user1.id
        }
        json_data = json.dumps(data)
        responce = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, responce.status_code)
        workout_1.refresh_from_db()
        self.assertEqual("Test workout Unittest", workout_1.name)

    def test_delete(self):
        workout_1 = Workout.objects.create(user=self.user1, name='Test workout 1')
        url = reverse('workout-detail', args=(workout_1.id,))
        data = {
            "name": "Test workout 1",
            "user": self.user1.id
        }
        json_data = json.dumps(data)
        responce = self.client.delete(url, data=json_data,
                                      content_type='application/json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, responce.status_code)


class ExerciseApiTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='test_user_1', password='testpassword')
        self.user2 = User.objects.create_user(username='test_user_2', password='testpassword')
        self.client.login(username='test_user_1', password='testpassword')
        self.workout_1 = Workout.objects.create(user=self.user1, name='Test workout 1')

    def test_get(self):

        exercise_1 = Exercise.objects.create(workout_connection=self.workout_1, name='Test exercise 1',
                                             sets=4,reps=10,weight=30)
        exercise_2 = Exercise.objects.create(workout_connection=self.workout_1, name='Test exercise 2',
                                            sets=4,reps=15,weight=40)
        url = reverse('exercise-list')
        responce = self.client.get(url)
        serializer_data = ExerciseSerializer([exercise_1, exercise_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, responce.status_code)
        self.assertEqual(serializer_data, responce.data)