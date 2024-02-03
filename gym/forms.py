from django import forms
from .models import UserProfile, WorkoutLog

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'weight', 'height', 'fitness_level', 'fitness_preference', 'fitness_goal']

class WorkoutLogForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ['exercise_type', 'duration', 'sets', 'reps', 'intensity']