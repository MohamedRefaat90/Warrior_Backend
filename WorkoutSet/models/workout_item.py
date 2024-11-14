from django.db import models
from Exercises.models import Exercise
from .workout_set import WorkoutSet

class WorkoutItem(models.Model):
    
    class Meta:
        db_table = "WorkoutItem"
    
    EQUIPMENT_CHOICES = [
        ('free_weight', 'Free Weight'),
        ('machine', 'Machine')
    ]
    
    FREE_WEIGHTS = [2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25, 27.5, 30, 32.5, 35, 37.5, 40, 42.5, 45, 47.5, 50]
    MACHINE_WEIGHTS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    workout_set = models.ForeignKey(WorkoutSet, on_delete=models.CASCADE, related_name='workout_items')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='workout_items')
    last_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    equipment_type = models.CharField(max_length=50, choices=EQUIPMENT_CHOICES, default='free_weight')
    
    def __str__(self):
        return f"{self.workout_set.name} - {self.exercise.name} - Last Weight: {self.last_weight} - Equipment: {self.get_equipment_type_display()}"
