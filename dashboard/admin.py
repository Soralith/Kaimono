from django.contrib import admin
from .models import WishlistItem, LibraryGame


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "action", "created_at")
    list_filter = ("category", "action")


@admin.register(LibraryGame)
class LibraryGameAdmin(admin.ModelAdmin):
    list_display = ("title", "studio", "status", "meta")
    list_filter = ("status",)