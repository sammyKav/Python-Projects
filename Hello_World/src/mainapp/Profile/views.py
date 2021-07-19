from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Profile

def admin_console(request):
    profiles = Profile.objects.all()
    return render(request, 'Profile/profiles.html', {'Profiles': profiles})