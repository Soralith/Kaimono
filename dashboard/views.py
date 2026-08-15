from django.shortcuts import render

def landing(request):
    return render(request, 'dashboard/pages/landing.html')

def index(request):
    return render(request, 'dashboard/pages/login.html')

def accsetup(request):
    return render(request, 'dashboard/pages/accsetup.html')

def dashboard(request):
    return render(request, 'dashboard/pages/dashboard.html')

def community(request):
    return render(request, 'dashboard/pages/community.html')

def profile(request):
    return render(request, 'dashboard/pages/profile.html')

def wishlist(request):
    return render(request, 'dashboard/pages/wishlist.html')

def library(request):
    return render(request, 'dashboard/pages/library.html')

def settings(request):
    return render(request, 'dashboard/pages/settings.html')