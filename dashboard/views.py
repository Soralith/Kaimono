from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from .models import WishlistItem, LibraryGame

def landing(request):
    return render(request, 'dashboard/pages/landing.html')

def dashboard(request):
    context = {
        'today': timezone.now()
    }
    return render(request, 'dashboard/pages/dashboard.html', context)

def shop(request):
    return render(request, 'dashboard/pages/shop.html')

def game_detail(request, product_id):
    return render(request, 'dashboard/pages/game_detail.html', {'product_id': product_id})

def community(request):
    return render(request, 'dashboard/pages/community.html')

def wishlist(request):
    items = list(WishlistItem.objects.all().order_by('created_at'))
    on_sale = [i for i in items if i.on_sale()]
    total_value = sum((i.price or 0) for i in items if i.price)
    savings = sum(((i.list_price or 0) - (i.price or 0)) for i in on_sale)
    games = [i for i in items if "Game" in i.category or "Indie" in i.category]
    merch = [i for i in items if "Figure" in i.category or "Artbook" in i.category]
    bundles = [i for i in items if "Bundle" in i.category]
    ctx = {
        "items": items,
        "total_count": len(items),
        "on_sale_count": len(on_sale),
        "total_value": total_value,
        "savings": savings,
        "games_count": len(games),
        "merch_count": len(merch),
        "bundles_count": len(bundles),
    }
    return render(request, 'dashboard/pages/wishlist.html', ctx)

def library(request):
    games = list(LibraryGame.objects.order_by('created_at'))
    installed = [g for g in games if g.status != "Not Installed"]
    favorites = [g for g in games if g.favorite]
    now_playing = next((g for g in games if g.status == "Now Playing"), installed[0] if installed else None)
    ctx = {
        "games": games,
        "total_count": len(games),
        "installed_count": len(installed),
        "ready_count": len(installed),
        "recent_count": len([g for g in games if g.status != "Not Installed"]),
        "favorites_count": len(favorites),
        "now_playing": now_playing,
    }
    return render(request, 'dashboard/pages/library.html', ctx)