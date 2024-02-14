from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, WorkoutLogForm, ProgressTrackingForm, FitnessGoalForm, NutritionLogForm

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

def set_fitness_goal(request):
    if request.method == 'POST':
        form = FitnessGoalForm(request.POST)
        if form.is_valid():
            fitness_goal = form.save(commit=False)
            fitness_goal.user_profile = request.user.userprofile  # Assuming user has a profile
            fitness_goal.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = FitnessGoalForm()

    return render(request, 'core/set_fitness_goal.html', {'form': form})

def log_nutrition(request):
    if request.method == 'POST':
        form = NutritionLogForm(request.POST)
        if form.is_valid():
            nutrition_log = form.save(commit=False)
            nutrition_log.user_profile = request.user.userprofile  # Assuming user has a profile
            nutrition_log.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = NutritionLogForm()

    return render(request, 'core/log_nutrition.html', {'form': form})