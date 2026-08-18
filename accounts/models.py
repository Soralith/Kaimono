from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('gamer', 'Gamer'),
        ('developer', 'Developer'),
    ]
    THEME_CHOICES = [
        ('midnight', 'Midnight'),
        ('silver', 'Silver'),
        ('paper', 'Paper'),
        ('obsidian', 'Obsidian'),
    ]

    display_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='gamer')
    bio = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)
    twitch = models.CharField(max_length=100, blank=True)
    avatar_url = models.URLField(blank=True)
    banner_url = models.URLField(blank=True)
    banner_position = models.IntegerField(default=50)
    theme = models.CharField(max_length=20, choices=THEME_CHOICES, default='silver')
    sidebar_expanded = models.BooleanField(default=False)
    reduce_animations = models.BooleanField(default=False)
    compact_mode = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.display_name or self.username} (@{self.username})'
