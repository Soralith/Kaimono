import re
from django import forms

from accounts.models import User
from .models import CommunityChannel


CATEGORY_CHOICES = [
    ("games", "Games"),
]


YOUTUBE_RE = re.compile(
    r'(?:youtube\.com/(?:watch\?v=|embed/|shorts/)|youtu\.be/)([A-Za-z0-9_-]{6,})'
)


def youtube_info(url):
    """Given a YouTube watch/short/embed link, return the embed URL + thumbnail.

    Returns None when the value isn't a YouTube link.
    """
    url = (url or '').strip()
    m = YOUTUBE_RE.search(url)
    if not m:
        return None
    vid = m.group(1)
    return {
        'embed': f'https://www.youtube.com/embed/{vid}',
        'thumb': f'https://img.youtube.com/vi/{vid}/hqdefault.jpg',
    }


def _split_csv(value):
    return [s.strip() for s in (value or "").split(",") if s.strip()]


def _to_float(value, default=None):
    try:
        value = float(value)
        return None if value != value else value
    except (TypeError, ValueError):
        return default


class MultipleImageInput(forms.ClearableFileInput):
    """File input that collects every uploaded file for a field into a list."""
    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        if self.allow_multiple_selected:
            return files.getlist(name)
        return files.get(name)


class MultipleImageField(forms.FileField):
    """Accepts several uploaded images (from a `multiple` file input)."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleImageInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        if data in (None, [], (), ""):
            return []
        if not isinstance(data, (list, tuple)):
            data = [data]
        cleaned = []
        for f in data:
            if f:
                cleaned.append(forms.ImageField().clean(f))
        return cleaned

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs["multiple"] = True
        return attrs


class AdminProductForm(forms.Form):
    """Create/update a shop product. A full `data` JSON is assembled from the
    structured fields so the game_detail / shop pages keep working."""
    name = forms.CharField(max_length=200)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    brand = forms.CharField(max_length=120, required=False)
    type = forms.CharField(max_length=80, required=False, help_text="e.g. Action RPG, PVC Statue")
    price = forms.DecimalField(max_digits=8, decimal_places=2, required=False)
    original_price = forms.DecimalField(max_digits=8, decimal_places=2, required=False)
    stock = forms.CharField(max_length=120, required=False)
    badges = forms.CharField(max_length=200, required=False, help_text="Comma separated, e.g. -50%, New")
    rating = forms.DecimalField(max_digits=3, decimal_places=1, required=False)
    reviews = forms.IntegerField(min_value=0, required=False)
    popularity = forms.IntegerField(min_value=0, required=False)
    image = forms.URLField(required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}), required=False)
    developer = forms.CharField(max_length=120, required=False)
    publisher = forms.CharField(max_length=120, required=False)
    release_date = forms.CharField(max_length=80, required=False)
    tags = forms.CharField(max_length=200, required=False, help_text="Comma separated")
    is_active = forms.BooleanField(required=False, initial=True)
    image_file = forms.ImageField(required=False)
    screenshot_files = MultipleImageField(required=False)
    trailer_url = forms.URLField(required=False, help_text="YouTube link (watch, short, or embed)")


    def build_data(self, product_id=None):
        from django.utils import timezone
        cd = self.cleaned_data
        price = _to_float(cd.get("price"))
        original_price = _to_float(cd.get("original_price"))
        rating = _to_float(cd.get("rating"))
        image = cd.get("image", "") or ""
        return {
            "id": product_id,
            "name": cd["name"],
            "brand": cd.get("brand") or "",
            "category": cd["category"],
            "type": cd.get("type") or "",
            "price": price,
            "originalPrice": original_price,
            "rating": rating if rating is not None else 0.0,
            "reviews": cd.get("reviews") or 0,
            "stock": cd.get("stock") or "",
            "badges": _split_csv(cd.get("badges")),
            "image": image,
            "popularity": cd.get("popularity") or 0,
            "date": timezone.now().date().isoformat(),
            "description": cd.get("description") or "",
            "releaseDate": cd.get("release_date") or "",
            "developer": cd.get("developer") or "",
            "publisher": cd.get("publisher") or cd.get("brand") or "",
            "tags": _split_csv(cd.get("tags")),
            "media": [],
            "screenshots": [image] if image else [],
            "friends": [],
            "bundles": [],
            "active": cd.get("is_active", True),
        }

    def build_media(self, existing_media=None):
        """Build the media list: the trailer first (if any), then existing media."""
        trailer_url = (self.cleaned_data.get("trailer_url") or "").strip()
        trailer = youtube_info(trailer_url)
        existing_media = existing_media or []
        # Existing youtube entries are replaced by whatever is in the field now
        # (a link re-populates the trailer; an empty field removes it).
        kept = [m for m in existing_media if not m.get("youtube")]
        if trailer:
            return [{
                "type": "video",
                "src": trailer["embed"],
                "poster": trailer["thumb"],
                "label": "Trailer",
                "youtube": True,
                "url": trailer_url,
            }] + kept
        return kept


class AdminUserForm(forms.ModelForm):
    password = forms.CharField(required=False, min_length=8,
                               widget=forms.PasswordInput(),
                               help_text="Leave blank to keep the current password")

    class Meta:
        model = User
        fields = ("username", "display_name", "email", "role", "is_staff", "is_active")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        qs = User.objects.exclude(pk=self.instance.pk).filter(email=email)
        if qs.exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        qs = User.objects.exclude(pk=self.instance.pk).filter(username=username)
        if qs.exists():
            raise forms.ValidationError("This username is taken.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class AdminChannelForm(forms.ModelForm):
    class Meta:
        model = CommunityChannel
        fields = ("name", "slug", "icon", "is_active")


class AdminMemberForm(forms.Form):
    username = forms.CharField(max_length=60)
    display_name = forms.CharField(max_length=80, required=False)
    avatar_url = forms.URLField(required=False)
    role = forms.ChoiceField(choices=[("gamer", "Gamer"), ("developer", "Developer")])
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}), required=False)
    is_online = forms.BooleanField(required=False)