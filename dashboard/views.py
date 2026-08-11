from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/pages/login.html')

def dashboard(request):
    return render(request, 'dashboard/pages/dashboard.html')