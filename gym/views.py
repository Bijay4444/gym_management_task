from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, WorkoutLogForm, ProgressTrackingForm

# Create your views here.
# @login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            return redirect('profile_detail')
    else:
        form = UserProfileForm()
        
    return render(request, 'core/create_profile.html', {'form': form})

def log_workout(request):
    if request.method == 'POST':
        form = WorkoutLogForm(request.POST)
        if form.is_valid():
            workout_log = form.save(commit=False)
            workout_log.user_profile = request.user.userprofile  # Assuming user has a profile
            workout_log.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = WorkoutLogForm()

    return render(request, 'core/log_workout.html', {'form': form})

def track_progress(request):
    if request.method == 'POST':
        form = ProgressTrackingForm(request.POST)
        if form.is_valid():
            progress_tracking = form.save(commit=False)
            progress_tracking.user_profile = request.user.userprofile  # Assuming user has a profile
            progress_tracking.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = ProgressTrackingForm()

    return render(request, 'core/track_progress.html', {'form': form})