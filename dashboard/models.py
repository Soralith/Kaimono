from django.db import models
from django.conf import settings


# ── Wishlist & Library (existing) ──────────────────────────────────

class UserWishlistItem(models.Model):
    """Per-user wishlist — links a user to a ShopProduct."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wishlist_items",
    )
    product = models.ForeignKey(
        'ShopProduct',
        on_delete=models.CASCADE,
        related_name="wishlisted_by",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} wishes {self.product}"


class WishlistItem(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    image_url = models.URLField()
    badge = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    tags = models.TextField(blank=True, help_text="Comma-separated tags")
    list_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    price_label = models.CharField(max_length=50, blank=True)
    rating = models.CharField(max_length=10, blank=True)
    action = models.CharField(max_length=50, default="Add to Cart")
    added_date = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def tag_list(self):
        return [t.strip() for t in self.tags.split(",") if t.strip()]

    def on_sale(self):
        return bool(self.list_price and self.price)

    def __str__(self):
        return self.title


class LibraryGame(models.Model):
    title = models.CharField(max_length=200)
    studio = models.CharField(max_length=100)
    image_url = models.URLField()
    meta = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, default="Installed")
    badge = models.CharField(max_length=50, blank=True)
    favorite = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="library_games",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ShopProduct(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    original_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.URLField(blank=True)
    data = models.JSONField(default=dict, help_text="Full product object (badges, media, screenshots, bundles, etc.)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Shop product"

    def __str__(self):
        return self.name


# ── Developer Submissions ───────────────────────────────────────

class GameSubmission(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    developer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='game_submissions',
    )
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=30, default='games')
    type = models.CharField(max_length=100, blank=True, help_text='e.g. Action RPG, Metroidvania')
    brand = models.CharField(max_length=100, blank=True, help_text='Studio / publisher name')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    original_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.URLField(blank=True, help_text='Banner / capsule image URL')
    description = models.TextField(blank=True)
    tags = models.CharField(max_length=300, blank=True, help_text='Comma-separated tags')
    trailer_url = models.URLField(blank=True, help_text='YouTube trailer URL')
    stock = models.CharField(max_length=100, blank=True, default='In Stock')
    badges = models.CharField(max_length=200, blank=True, help_text='Comma-separated badges')
    developer_name = models.CharField(max_length=100, blank=True, help_text='Developer credit shown on product')
    publisher = models.CharField(max_length=100, blank=True)
    release_date = models.CharField(max_length=60, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    admin_note = models.TextField(blank=True, help_text='Admin feedback note')
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.status}) by {self.developer}"

    def to_product_data(self):
        """Build the ShopProduct.data dict from this submission."""
        tags_list = [t.strip() for t in self.tags.split(',') if t.strip()]
        badges_list = [b.strip() for b in self.badges.split(',') if b.strip()]
        media = []
        if self.trailer_url:
            media.append({'url': self.trailer_url, 'youtube': True})
        return {
            'name': self.name,
            'category': self.category,
            'type': self.type,
            'brand': self.brand,
            'price': float(self.price) if self.price else 0,
            'originalPrice': float(self.original_price) if self.original_price else None,
            'image': self.image,
            'description': self.description,
            'tags': tags_list,
            'badges': badges_list,
            'stock': self.stock or 'In Stock',
            'developer': self.developer_name or self.brand,
            'publisher': self.publisher,
            'releaseDate': self.release_date,
            'rating': 0,
            'reviews': 0,
            'popularity': 0,
            'date': str(self.created_at.date()) if self.created_at else '',
            'screenshots': [self.image] if self.image else [],
            'media': media,
            'friends': [],
            'bundles': [],
            'active': True,
        }


# ── Community ──────────────────────────────────────────────────────

class CommunityStory(models.Model):
    username = models.CharField(max_length=60)
    avatar_url = models.URLField()
    is_seen = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"@{self.username}"


class CommunityChannel(models.Model):
    ICON_CHOICES = [
        ("hash", "hash"),
        ("image", "image"),
        ("palette", "palette"),
        ("book-open", "book-open"),
        ("gamepad-2", "gamepad-2"),
        ("shopping-bag", "shopping-bag"),
        ("sparkles", "sparkles"),
        ("megaphone", "megaphone"),
        ("message-circle", "message-circle"),
    ]
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=30, choices=ICON_CHOICES, default="hash")
    post_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"#{self.name}"


class CommunityGame(models.Model):
    name = models.CharField(max_length=120)
    image_url = models.URLField()
    is_active = models.BooleanField(default=False, help_text="Show live dot")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class CommunityPost(models.Model):
    POST_TYPES = [
        ("announcement", "Announcement"),
        ("image", "Image Post"),
        ("poll", "Poll"),
        ("discussion", "Discussion"),
        ("guide", "Guide"),
    ]

    post_type = models.CharField(max_length=20, choices=POST_TYPES)
    title = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    author_name = models.CharField(max_length=80)
    author_avatar = models.URLField()
    author_badge = models.CharField(max_length=30, blank=True, help_text="e.g. verified, admin")
    channel = models.ForeignKey(
        CommunityChannel, on_delete=models.SET_NULL, null=True, blank=True
    )
    is_pinned = models.BooleanField(default=False)
    time_ago = models.CharField(max_length=30, blank=True, help_text="e.g. '2 hours ago'")
    visibility = models.CharField(max_length=20, default="Public")

    # Engagement counters
    reaction_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    bookmark_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_pinned", "-created_at"]

    def __str__(self):
        return f"[{self.post_type}] {self.title or self.content[:60]}"


class PostImage(models.Model):
    """One or more images attached to a post."""
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name="images")
    url = models.URLField()
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]


class PostTag(models.Model):
    """Tags / hashtags for a post."""
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name="tags")
    name = models.CharField(max_length=40)
    is_highlighted = models.BooleanField(default=False, help_text="Use brand badge style")

    def __str__(self):
        return f"#{self.name}"


class PostReaction(models.Model):
    """Which reaction types a post received (for display only)."""
    REACTION_TYPES = [
        ("heart", "Heart"),
        ("thumbs-up", "Thumbs Up"),
        ("camera", "Camera"),
        ("star", "Star"),
    ]
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name="reaction_types")
    reaction_type = models.CharField(max_length=20, choices=REACTION_TYPES)

    def __str__(self):
        return f"{self.reaction_type} on {self.post}"


# ── Poll (linked 1-to-1 with post_type='poll') ────────────────────

class Poll(models.Model):
    post = models.OneToOneField(CommunityPost, on_delete=models.CASCADE, related_name="poll")
    question = models.CharField(max_length=300)
    total_votes = models.IntegerField(default=0)
    time_left = models.CharField(max_length=30, blank=True, help_text="e.g. '3 days left'")

    def __str__(self):
        return self.question


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options")
    label = models.CharField(max_length=120)
    percentage = models.IntegerField(default=0)
    is_selected = models.BooleanField(default=False, help_text="Whether current user selected")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.label} ({self.percentage}%)"


# ── User Interactions ──────────────────────────────────────────────

from django.conf import settings


class PollVote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="votes")
    option = models.ForeignKey(PollOption, on_delete=models.CASCADE, related_name="votes")
    user_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("poll", "user_name")

    def __str__(self):
        return f"{self.user_name} → {self.option.label}"


class CommunityComment(models.Model):
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(max_length=80)
    author_avatar = models.URLField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.author_name}: {self.content[:40]}"


class UserLike(models.Model):
    user_name = models.CharField(max_length=80)
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name="user_likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user_name", "post")

    def __str__(self):
        return f"{self.user_name} liked {self.post}"


class UserBookmark(models.Model):
    user_name = models.CharField(max_length=80)
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name="user_bookmarks")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user_name", "post")

    def __str__(self):
        return f"{self.user_name} saved {self.post}"


# ── Community: followed games & friends ─────────────────────────────

class UserFollowedGame(models.Model):
    """Which community games the current user follows."""
    user_name = models.CharField(max_length=80)
    game = models.ForeignKey(CommunityGame, on_delete=models.CASCADE, related_name="follows")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user_name", "game")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user_name} follows {self.game.name}"


class CommunityMember(models.Model):
    """A community friend / member with a mini profile preview."""
    ROLE_CHOICES = [
        ("gamer", "Gamer"),
        ("developer", "Developer"),
    ]
    username = models.CharField(max_length=60)
    display_name = models.CharField(max_length=80, blank=True)
    avatar_url = models.URLField(blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="gamer")
    bio = models.TextField(blank=True)
    is_online = models.BooleanField(default=False)
    last_active = models.CharField(max_length=40, blank=True, help_text="e.g. '2m ago'")
    level = models.IntegerField(default=1)
    games_played = models.IntegerField(default=0)
    achievements = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    member_since = models.CharField(max_length=40, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["-is_online", "order"]

    def __str__(self):
        return self.display_name or self.username
