# gym/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    FITNESS_PREFERENCES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('overall_health', 'Overall Health'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    fitness_level = models.CharField(max_length=255)
    fitness_preference = models.CharField(max_length=255, choices=FITNESS_PREFERENCES)
    fitness_goal = models.CharField(max_length=255, choices=FITNESS_PREFERENCES)


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    # ... other fields

class Workout(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    duration = models.DurationField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    intensity = models.CharField(max_length=255)
    # ... other fields
