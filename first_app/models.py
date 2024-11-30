from django.db import models
from datetime import date

# Create your models here.
 
class Student(models.Model):
    name=models.CharField(max_length=50)   #max lenght must bole dite hoi
    roll=models.IntegerField(primary_key=True)     
    age=models.IntegerField(default=18)
    date=models.DateField(default=date.today)
    address=models.TextField(max_length=255)
    even_duration=models.DurationField(null=True, blank=True)
  
    
    def __str__(self):
        return f"{self.name}"  # object er specific kono value call na korle se ei string return korbe2