from django.db import models

class Muscle(models.Model):
    
    class Meta:
        db_table = "Muscle"
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to= "Muscles/" ,null= True , blank=True)
    
    def __str__(self):
        return self.name