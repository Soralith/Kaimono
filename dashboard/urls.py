from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.index, name='login'),
    path('accsetup/', views.accsetup, name='accsetup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('community/', views.community, name='community'),
    path('profile/', views.profile, name='profile'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('library/', views.library, name='library'),
    path('settings/', views.settings, name='settings'),
]