from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache

from . import storage
from .forms import AccountSetupForm, ProfileForm, RegisterForm, SettingsForm
from .models import User


def logout_view(request):
    logout(request)
    return redirect('landing')


@never_cache
def login_view(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        # Users sign in with their email address.
        try:
            target = User.objects.get(email=email)
        except User.DoesNotExist:
            target = None
        user = authenticate(request, username=target.username, password=password) if target else None
        if user is not None:
            login(request, user)
            if user.display_name:
                return redirect('dashboard')
            return redirect('accsetup')
        error = 'Invalid email or password.'
    return render(request, 'dashboard/pages/login.html', {'error': error})


@never_cache
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accsetup')
        return render(request, 'dashboard/pages/login.html', {'register_error': True})
    return redirect('login')


@never_cache
def accsetup_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = AccountSetupForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        if form.cleaned_data.get('avatar'):
            user.avatar_url = storage.upload_image(form.cleaned_data['avatar'], folder='avatars')
        if form.cleaned_data.get('banner'):
            user.banner_url = storage.upload_image(form.cleaned_data['banner'], folder='banners')
        user.save()
        messages.success(request, 'Account updated.')
        return redirect('dashboard')

    return render(request, 'dashboard/pages/accsetup.html', {'form': form})


@never_cache
def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        if form.cleaned_data.get('avatar'):
            user.avatar_url = storage.upload_image(form.cleaned_data['avatar'], folder='avatars')
        if form.cleaned_data.get('banner'):
            user.banner_url = storage.upload_image(form.cleaned_data['banner'], folder='banners')
        user.save()
        messages.success(request, 'Profile saved.')
        return redirect('profile')

    return render(request, 'dashboard/pages/profile.html', {'form': form})


@never_cache
def settings_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = SettingsForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        if request.POST.get('avatar_remove'):
            user.avatar_url = ''
        elif form.cleaned_data.get('avatar'):
            user.avatar_url = storage.upload_image(form.cleaned_data['avatar'], folder='avatars')
        user.save()
        messages.success(request, 'Settings saved.')
        return redirect('settings')

    return render(request, 'dashboard/pages/settings.html', {'form': form})


@never_cache
def delete_account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        # Get the current user before logout
        user = request.user
        # Logout first to avoid session issues
        logout(request)
        # Delete the user permanently
        user.delete()
        messages.success(request, 'Your account has been permanently deleted.')
        return redirect('landing')

    # If GET, redirect to settings
    return redirect('settings')