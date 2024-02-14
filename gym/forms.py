from django import forms
from .models import UserProfile, WorkoutLog, ProgressTracking, FitnessGoal, NutritionLog

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'weight', 'height', 'fitness_level', 'fitness_preference', 'fitness_goal']

class WorkoutLogForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ['exercise_type', 'duration', 'sets', 'reps', 'intensity']
        
class ProgressTrackingForm(forms.ModelForm):
    class Meta:
        model = ProgressTracking
        fields = ['weight', 'body_measurements', 'fitness_level']
        
class FitnessGoalForm(forms.ModelForm):
    class Meta:
        model = FitnessGoal
        fields = ['description', 'target_date']
        
class NutritionLogForm(forms.ModelForm):
    class Meta:
        model = NutritionLog
        fields = ['meal_description', 'calories']