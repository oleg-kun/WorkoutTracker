from django.shortcuts import render

from workouts.models import Workout


# Create your views here.

def all_workouts_view(request):
    return render(request, 'all_workouts.html', { 'all_workouts' : Workout.objects.all()})


def exercise_view(request):
    pass
