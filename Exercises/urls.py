from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"Muscles", MuclseView, basename="Muscles")
router.register(r"Exercises", ExercisesView, basename="Exercises")

urlpatterns = [
    path('', include(router.urls))
]
