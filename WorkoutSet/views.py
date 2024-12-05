from rest_framework import generics
from .models.workout_set import WorkoutSet
from .serializer import WorkoutSetSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class WorkoutSetCreateView(generics.CreateAPIView):
    queryset = WorkoutSet.objects.all()
    serializer_class = WorkoutSetSerializer
    permission_classes = [IsAuthenticated]