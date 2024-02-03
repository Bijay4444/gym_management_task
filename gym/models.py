# Description: This file contains the models for the gym app.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    FITNESS_PREFERENCES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('overall_health', 'Overall Health'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    fitness_level = models.CharField(max_length=255)
    fitness_preference = models.CharField(max_length=255, choices=FITNESS_PREFERENCES)
    fitness_goal = models.CharField(max_length=255, choices=FITNESS_PREFERENCES)


class WorkoutLog(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    exercise_type = models.CharField(max_length=255)
    duration = models.DurationField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    intensity = models.CharField(max_length=255)
    log_date = models.DateTimeField(auto_now_add=True)
