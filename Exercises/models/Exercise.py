from django.db import models
from ..helpers import *

# Create your models here.

class Exercise(models.Model):
    
    class Meta:
        db_table = "Exercise"
    
    TYPE = [
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility')
    ]
    

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    gif = models.ImageField(upload_to="gifs/", null=True, blank=True)
    type = models.CharField(max_length=100, choices=TYPE, null=True)
    muscle = models.ForeignKey('Muscle', on_delete=models.CASCADE, related_name='exercises', null=True)
    
    
    def __str__(self):
        return self.name