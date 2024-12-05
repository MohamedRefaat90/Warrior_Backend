from django.shortcuts import render
from rest_framework import viewsets
from .models import Muscle, Exercise
from .serializer import MuscleSerializer, ExerciseSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class MuclseView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
    

class ExercisesView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
