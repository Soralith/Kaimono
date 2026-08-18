"""Vercel serverless entry point for the Django WSGI app."""

import os
import sys

# Ensure the project root is on the path so Django modules are importable.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kaimono.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
