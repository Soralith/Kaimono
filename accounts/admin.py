from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class KaimonoUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Kaimono profile', {'fields': ('display_name', 'age', 'role', 'avatar_url', 'banner_url')}),
    )
