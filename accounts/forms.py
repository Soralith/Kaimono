from django import forms

from .models import User


class RegisterForm(forms.ModelForm):
    display_name = forms.CharField(
        max_length=60,
        required=True,
        label='Full name',
        widget=forms.TextInput(),
    )
    email = forms.EmailField(required=True, label='Email address')
    password = forms.CharField(
        min_length=8,
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Min. 8 characters'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'display_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['email']
        user.display_name = self.cleaned_data['display_name']
        if commit:
            user.save()
        return user


class AccountSetupForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))
    banner = forms.ImageField(required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = User
        fields = ('display_name', 'username', 'age', 'role', 'email')

    def clean_display_name(self):
        display_name = self.cleaned_data.get('display_name')
        if not display_name or not display_name.strip():
            raise forms.ValidationError('Full name is required.')
        return display_name.strip()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            raise forms.ValidationError('Age is required.')
        if age < 18:
            raise forms.ValidationError('You must be at least 18 years old to create an account.')
        return age

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required.')
        return email


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))
    banner = forms.ImageField(required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = User
        fields = ('display_name', 'username', 'role', 'bio')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username


class SettingsForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = User
        fields = ('display_name', 'bio', 'theme', 'sidebar_expanded', 'reduce_animations', 'compact_mode')