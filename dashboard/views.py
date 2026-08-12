from django.shortcuts import render

def landing(request):
    return render(request, 'dashboard/pages/landing.html')

def index(request):
    return render(request, 'dashboard/pages/login.html')

def dashboard(request):
    return render(request, 'dashboard/pages/dashboard.html')