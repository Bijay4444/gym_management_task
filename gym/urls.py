from django.urls import path
from .views import create_profile, log_workout, track_progress, set_fitness_goal, log_nutrition

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    path('log_workout/', log_workout, name='log_workout'),
    path('track_progress/', track_progress, name='track_progress'),
    path('set_fitness_goal/', set_fitness_goal, name='set_fitness_goal'),
    path('log_nutrition/', log_nutrition, name='log_nutrition')
]
