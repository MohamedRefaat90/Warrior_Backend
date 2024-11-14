from rest_framework import serializers
from .models import Exercise, Muscle

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
        
class MuscleSerializer(serializers.ModelSerializer):
    exercise_count = serializers.SerializerMethodField()
    class Meta:
        model = Muscle
        fields = '__all__'
        
    def get_exercise_count(self, obj) -> int:
        return obj.exercises.count()