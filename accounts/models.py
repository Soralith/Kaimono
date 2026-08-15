from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('gamer', 'Gamer'),
        ('developer', 'Developer'),
    ]

    display_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='gamer')
    bio = models.CharField(max_length=200, blank=True)
    avatar_url = models.URLField(blank=True)
    banner_url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.display_name or self.username} (@{self.username})'
