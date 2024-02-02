from django import forms
from .models import UserProfile 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'weight', 'height', 'fitness_level', 'fitness_preference', 'fitness_goal']