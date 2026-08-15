from django.shortcuts import render

def landing(request):
    return render(request, 'dashboard/pages/landing.html')

def dashboard(request):
    return render(request, 'dashboard/pages/dashboard.html')

def shop(request):
    return render(request, 'dashboard/pages/shop.html')

def game_detail(request, product_id):
    return render(request, 'dashboard/pages/game_detail.html', {'product_id': product_id})

def community(request):
    return render(request, 'dashboard/pages/community.html')

def wishlist(request):
    return render(request, 'dashboard/pages/wishlist.html')

def library(request):
    return render(request, 'dashboard/pages/library.html')