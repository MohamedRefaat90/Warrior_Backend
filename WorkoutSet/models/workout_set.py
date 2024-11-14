from django.db import models
from User.models import Users
from Exercises.models import Exercise

# Create your models here.

class WorkoutSet(models.Model):
    
    class Meta:
        db_table = 'WorkoutSet'
    
    WORKOUT_TYPE_CHOICES  = [
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility')
    ]
    
    name = models.CharField(max_length=50)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='workout_sets')
    description = models.TextField(blank=True)
    workout_type = models.CharField(max_length=50,choices=WORKOUT_TYPE_CHOICES )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name