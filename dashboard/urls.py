from django.urls import path
from django.contrib.auth.decorators import login_required

from accounts import views as auth
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', auth.login_view, name='login'),
    path('register/', auth.register_view, name='register'),
    path('logout/', auth.logout_view, name='logout'),
    path('accsetup/', auth.accsetup_view, name='accsetup'),
    path('profile/', login_required(auth.profile_view), name='profile'),
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:product_id>/', views.game_detail, name='game_detail'),
    path('community/', views.community, name='community'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('library/', views.library, name='library'),
    path('settings/', login_required(auth.settings_view), name='settings'),
    path('settings/delete-account/', login_required(auth.delete_account_view), name='delete_account'),
]