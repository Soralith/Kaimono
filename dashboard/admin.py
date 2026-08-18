from django.contrib import admin
from .models import (
    WishlistItem, UserWishlistItem, LibraryGame, ShopProduct,
    CommunityStory, CommunityChannel, CommunityGame,
    CommunityPost, PostImage, PostTag, PostReaction,
    Poll, PollOption, CommunityMember, UserFollowedGame,
)


@admin.register(UserWishlistItem)
class UserWishlistItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "created_at")
    list_filter = ("created_at",)
    raw_id_fields = ("user", "product")


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "action", "created_at")
    list_filter = ("category", "action")


@admin.register(LibraryGame)
class LibraryGameAdmin(admin.ModelAdmin):
    list_display = ("title", "studio", "status", "meta", "user")
    list_filter = ("status", "user")


@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "original_price")
    list_filter = ("category",)
    search_fields = ("name",)
    fields = ("id", "name", "category", "price", "original_price", "image", "data")
    readonly_fields = ("id",)


# ── Community ──────────────────────────────────────────────────────

@admin.register(CommunityStory)
class CommunityStoryAdmin(admin.ModelAdmin):
    list_display = ("username", "is_seen", "order")


@admin.register(CommunityChannel)
class CommunityChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "icon", "post_count", "is_active")


@admin.register(CommunityGame)
class CommunityGameAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "order")


@admin.register(CommunityMember)
class CommunityMemberAdmin(admin.ModelAdmin):
    list_display = ("display_name", "username", "role", "is_online", "level", "order")
    list_filter = ("role", "is_online")


@admin.register(UserFollowedGame)
class UserFollowedGameAdmin(admin.ModelAdmin):
    list_display = ("user_name", "game", "created_at")
    list_filter = ("user_name",)


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 0


class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 0


class PostReactionInline(admin.TabularInline):
    model = PostReaction
    extra = 0


@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ("title", "post_type", "author_name", "channel", "is_pinned", "created_at")
    list_filter = ("post_type", "is_pinned", "channel")
    inlines = [PostImageInline, PostTagInline, PostReactionInline]


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("question", "total_votes", "time_left")


@admin.register(PollOption)
class PollOptionAdmin(admin.ModelAdmin):
    list_display = ("label", "poll", "percentage", "is_selected", "order")
