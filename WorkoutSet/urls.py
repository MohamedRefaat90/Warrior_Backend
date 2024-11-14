from django.urls import path
from .views import WorkoutSetCreateView

urlpatterns = [
    path('Create/', WorkoutSetCreateView.as_view(), name='create_workout_set'),
]