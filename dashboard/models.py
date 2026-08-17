from django.db import models


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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title