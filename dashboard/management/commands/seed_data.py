from django.core.management.base import BaseCommand
from dashboard.models import WishlistItem, LibraryGame


class Command(BaseCommand):
    help = "Seed the database with demo wishlist items and library games."

    def handle(self, *args, **options):
        WishlistItem.objects.all().delete()
        LibraryGame.objects.all().delete()

        wishlist = [
            {
                "title": "NieR:Automata\u2122 GOTY Edition",
                "category": "Game",
                "image_url": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=400&q=80",
                "badge": "-50% OFF",
                "description": "Square Enix \u00b7 Action RPG \u00b7 Wishlist added Mar 2026",
                "tags": "Singleplayer,RPG",
                "list_price": "39.99",
                "price": "19.99",
                "rating": "4.9",
                "action": "Add to Cart",
            },
            {
                "title": "Genshin Impact: Best of Art 2026",
                "category": "Artbook",
                "image_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=400&q=80",
                "badge": "-40% OFF",
                "description": "HoYoverse \u00b7 Artbook \u00b7 Wishlist added Jun 2026",
                "tags": "Hardcover,Limited Edition",
                "list_price": "59.99",
                "price": "35.99",
                "action": "Add to Cart",
            },
            {
                "title": "Honkai: Star Rail",
                "category": "Game \u00b7 Free",
                "image_url": "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=400&q=80",
                "description": "HoYoverse \u00b7 Turn-Based RPG \u00b7 Wishlist added Aug 2025",
                "tags": "Gacha,Multiplayer",
                "rating": "4.8",
                "price_label": "Free to Play",
                "action": "Get Free",
            },
            {
                "title": "Monster Hunter World: Iceborne",
                "category": "Game",
                "image_url": "https://images.unsplash.com/photo-1614624532983-4ce03382d63d?auto=format&fit=crop&w=400&q=80",
                "badge": "-67% OFF",
                "description": "CAPCOM \u00b7 Action RPG \u00b7 Wishlist added Jan 2026",
                "tags": "Co-op,Hunting",
                "list_price": "29.99",
                "price": "9.89",
                "rating": "4.7",
                "action": "Add to Cart",
            },
            {
                "title": "Genshin Impact Venti Scale Figure",
                "category": "Figure",
                "image_url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=400&q=80",
                "badge": "-25% OFF",
                "description": "Good Smile Company \u00b7 1/7 Scale \u00b7 Wishlist added May 2026",
                "tags": "Pre-Painted,Ships in 2w",
                "list_price": "120.00",
                "price": "89.99",
                "action": "Add to Cart",
            },
            {
                "title": "Persona 3 Reload",
                "category": "Game",
                "image_url": "https://images.unsplash.com/photo-1592853625601-bb9d23da12fc?auto=format&fit=crop&w=400&q=80",
                "description": "ATLUS \u00b7 JRPG \u00b7 Wishlist added Feb 2026",
                "tags": "JRPG,Turn-Based",
                "rating": "4.8",
                "price": "69.99",
                "action": "Notify on Drop",
            },
            {
                "title": "Cyberpunk 2077: Ultimate Edition",
                "category": "Game",
                "image_url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=400&q=80",
                "description": "CD Projekt RED \u00b7 Open World RPG \u00b7 Wishlist added Dec 2025",
                "tags": "Open World,Cyberpunk",
                "rating": "4.6",
                "price": "59.99",
                "action": "Notify on Drop",
            },
            {
                "title": "Project Sekai Ichika Nendoroid",
                "category": "Figure \u00b7 Pre-Order",
                "image_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=400&q=80",
                "description": "Good Smile \u00b7 Nendoroid \u00b7 Wishlist added Apr 2026",
                "tags": "Pre-Order,Ships Nov 2026",
                "price": "65.00",
                "action": "Pre-Order",
            },
            {
                "title": "Hollow Knight: Silksong",
                "category": "Indie Game",
                "image_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?auto=format&fit=crop&w=400&q=80",
                "description": "Team Cherry \u00b7 Metroidvania \u00b7 Wishlist added Jul 2026",
                "tags": "Metroidvania,2D,Coming Soon",
                "price_label": "TBA",
                "action": "Notify on Release",
            },
            {
                "title": "Persona 5 Royal Ultimate Bundle",
                "category": "Bundle \u00b7 3 Items",
                "image_url": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?auto=format&fit=crop&w=400&q=80",
                "description": "ATLUS \u00b7 Game + DLC + OST \u00b7 Wishlist added May 2026",
                "tags": "Bundle,JRPG",
                "rating": "4.9",
                "price": "89.99",
                "action": "Add to Cart",
            },
        ]

        for item in wishlist:
            WishlistItem.objects.create(**item)

        games = [
            {
                "title": "Project Sekai: Colorful Stage!",
                "studio": "SEGA",
                "image_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=400&q=80",
                "meta": "320h",
                "status": "Now Playing",
                "badge": "Now Playing",
            },
            {
                "title": "NieR:Automata\u2122",
                "studio": "Square Enix",
                "image_url": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=400&q=80",
                "meta": "85h",
                "status": "Installed",
            },
            {
                "title": "Honkai: Star Rail",
                "studio": "HoYoverse",
                "image_url": "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=400&q=80",
                "meta": "140h",
                "status": "Installed",
                "favorite": True,
            },
            {
                "title": "Genshin Impact",
                "studio": "HoYoverse",
                "image_url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=400&q=80",
                "meta": "56h",
                "status": "Installed",
                "badge": "Update",
            },
            {
                "title": "Elden Ring: Shadow",
                "studio": "FromSoftware",
                "image_url": "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=400&q=80",
                "meta": "210h",
                "status": "Installed",
                "badge": "GOTY",
                "favorite": True,
            },
            {
                "title": "Persona 3 Reload",
                "studio": "ATLUS",
                "image_url": "https://images.unsplash.com/photo-1592853625601-bb9d23da12fc?auto=format&fit=crop&w=400&q=80",
                "meta": "32h",
                "status": "Installed",
            },
            {
                "title": "Monster Hunter World",
                "studio": "CAPCOM",
                "image_url": "https://images.unsplash.com/photo-1614624532983-4ce03382d63d?auto=format&fit=crop&w=400&q=80",
                "meta": "45GB",
                "status": "Not Installed",
            },
            {
                "title": "Zelda: Tears of Kingdom",
                "studio": "Nintendo",
                "image_url": "https://images.unsplash.com/photo-1551103782-8ab07afd45c1?auto=format&fit=crop&w=400&q=80",
                "meta": "120h",
                "status": "Installed",
                "badge": "GOTY",
            },
            {
                "title": "Cyberpunk 2077",
                "studio": "CD Projekt",
                "image_url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=400&q=80",
                "meta": "89h",
                "status": "Installed",
            },
            {
                "title": "Hollow Knight",
                "studio": "Team Cherry",
                "image_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?auto=format&fit=crop&w=400&q=80",
                "meta": "67h",
                "status": "Installed",
                "favorite": True,
            },
            {
                "title": "Hades",
                "studio": "Supergiant",
                "image_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=400&q=80",
                "meta": "45h",
                "status": "Installed",
                "badge": "Indie Hit",
            },
            {
                "title": "Stardew Valley",
                "studio": "ConcernedApe",
                "image_url": "https://images.unsplash.com/photo-1488866022916-f7f2b3077a5c?auto=format&fit=crop&w=400&q=80",
                "meta": "2GB",
                "status": "Not Installed",
            },
        ]

        for game in games:
            LibraryGame.objects.create(**game)

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {WishlistItem.objects.count()} wishlist items and "
                f"{LibraryGame.objects.count()} library games."
            )
        )