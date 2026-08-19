from django.conf import settings


def site_images(request):
    """Make the Supabase site-images base URL available in every template as {{ SITE_IMAGES_URL }}."""
    return {"SITE_IMAGES_URL": settings.SUPABASE_SITE_IMAGES_URL}
