import uuid

import boto3
from botocore.client import Config
from django.conf import settings

ALLOWED_IMAGE_TYPES = {'image/jpeg': '.jpg', 'image/png': '.png', 'image/webp': '.webp', 'image/gif': '.gif'}


def _client():
    return boto3.client(
        's3',
        endpoint_url=settings.SUPABASE_S3_ENDPOINT,
        aws_access_key_id=settings.SUPABASE_S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings.SUPABASE_S3_SECRET_ACCESS_KEY,
        region_name=settings.SUPABASE_REGION,
        config=Config(signature_version='s3v4'),
    )


def public_url(key):
    bucket = settings.SUPABASE_S3_BUCKET
    return f'{settings.SUPABASE_URL}/storage/v1/object/public/{bucket}/{key}'


def upload_image(file_obj, folder='avatars'):
    """Upload an image to Supabase Storage and return its public URL.

    Returns the public URL, or '' if the file is missing/unsupported.
    """
    if not file_obj:
        return ''

    content_type = getattr(file_obj, 'content_type', '') or ''
    ext = ALLOWED_IMAGE_TYPES.get(content_type, '')
    if not ext:
        ext = '.jpg'

    key = f'{folder}/{uuid.uuid4().hex}{ext}'
    _client().upload_fileobj(
        file_obj,
        settings.SUPABASE_S3_BUCKET,
        key,
        ExtraArgs={'ACL': 'public-read', 'ContentType': content_type or 'image/jpeg'},
    )
    return public_url(key)