from django.shortcuts import render
from .models import Profile, Project


def home(request):
    # Keep the database empty until the owner adds their profile in Django admin.
    profile = Profile.objects.first() or Profile()
    return render(request, "portfolio/home.html", {"profile": profile, "projects": Project.objects.filter(featured=True)})
