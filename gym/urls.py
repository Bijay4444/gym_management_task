from django.urls import path
from .views import create_profile, log_workout, track_progress

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    path('log_workout/', log_workout, name='log_workout'),
    path('track_progress/', track_progress, name='track_progress'),
]
