from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

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