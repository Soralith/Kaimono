import json
import os
import re

from django.conf import settings
from django.core.management.base import BaseCommand
from decimal import Decimal

from dashboard.models import ShopProduct


class Command(BaseCommand):
    help = "Seed the shop table (dashboard_shop) from the static products.js catalog."

    def _load_products(self):
        path = os.path.join(settings.BASE_DIR, 'dashboard', 'static', 'dashboard', 'js', 'products.js')
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        match = re.search(r'window\.KAIMONO_PRODUCTS\s*=\s*(\[.*?\]);', text, re.DOTALL)
        if not match:
            raise ValueError('Could not locate KAIMONO_PRODUCTS array in products.js')
        raw = match.group(1)
        raw = re.sub(r'(?<=[\{,])\s*([A-Za-z_$][\w$]*)\s*:', r'"\1":', raw)
        raw = re.sub(r',\s*([}\]])', r'\1', raw)
        return json.loads(raw)

    def _decimal(self, value):
        if value is None:
            return None
        return Decimal(str(value))

    def handle(self, *args, **options):
        ShopProduct.objects.all().delete()
        products = self._load_products()

        rows = []
        for p in products:
            rows.append(
                ShopProduct(
                    id=int(p.get('id')),
                    name=p.get('name', ''),
                    category=p.get('category', ''),
                    price=self._decimal(p.get('price')),
                    original_price=self._decimal(p.get('originalPrice')),
                    image=p.get('image', ''),
                    data=p,
                )
            )
        ShopProduct.objects.bulk_create(rows)

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(rows)} shop products into dashboard_shop."))