"""Upload all site images (landing, game cards, defaults) to Supabase Storage."""

import os
import mimetypes

from django.conf import settings
from django.core.management.base import BaseCommand

from accounts.storage import _client, public_url

IMAGES_DIR = os.path.join(
    settings.BASE_DIR, "dashboard", "static", "dashboard", "images"
)

# Map local filename → Supabase Storage key
IMAGE_MAP = {
    # Hero slides
    "landing1.jpeg": "site/landing1.jpeg",
    "landing2.png": "site/landing2.png",
    "landing3.jpg": "site/landing3.jpg",
    "landing4.png": "site/landing4.png",
    # Collage / store sections
    "landing.png": "site/landing.png",
    "landingg.png": "site/landingg.png",
    # Game cards
    "clairobscur.jpg": "site/clairobscur.jpg",
    "silksong.jpg": "site/silksong.jpg",
    "baldursgate3.jpg": "site/baldursgate3.jpg",
    "spacefortheunbound.jpg": "site/spacefortheunbound.jpg",
    "ff16.jpeg": "site/ff16.jpeg",
    "rerequiem.jpg": "site/rerequiem.jpg",
    # Default avatar / banner
    "accsetup.jpg": "site/accsetup.jpg",
    "banner.jpg": "site/banner.jpg",
    # Extra
    "exastris.png": "site/exastris.png",
}


class Command(BaseCommand):
    help = "Upload site images to Supabase Storage"

    def handle(self, *args, **options):
        client = _client()
        bucket = settings.SUPABASE_S3_BUCKET
        uploaded = []

        for local_name, storage_key in IMAGE_MAP.items():
            local_path = os.path.join(IMAGES_DIR, local_name)
            if not os.path.exists(local_path):
                self.stdout.write(self.style.WARNING(f"  SKIP  {local_name} (not found)"))
                continue

            content_type = mimetypes.guess_type(local_name)[0] or "image/jpeg"
            client.upload_fileobj(
                open(local_path, "rb"),
                bucket,
                storage_key,
                ExtraArgs={
                    "ACL": "public-read",
                    "ContentType": content_type,
                },
            )
            url = public_url(storage_key)
            uploaded.append((local_name, url))
            self.stdout.write(self.style.SUCCESS(f"  OK    {local_name}  →  {url}"))

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(f"Uploaded {len(uploaded)} images."))

        # Print a mapping for easy copy-paste into settings / templates
        self.stdout.write("")
        self.stdout.write("── URL mapping ──")
        for name, url in uploaded:
            self.stdout.write(f'  "{name}": "{url}",')
