import datetime
import json
import math
import os
import re
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.db.models import Q, Count
from collections import defaultdict

from accounts.models import User
from .models import (
    WishlistItem, UserWishlistItem, LibraryGame, ShopProduct,
    GameSubmission, GameReview,
    CommunityStory, CommunityChannel, CommunityGame, CommunityPost,
    PostImage, PostTag, PostReaction, Poll, PollOption, PollVote,
    CommunityComment,
    CommunityMember, UserFollowedGame,
)
from .forms import AdminProductForm, AdminUserForm, AdminChannelForm, AdminMemberForm

POSTS_PER_PAGE = 5


def _get_username(request):
    """Return a demo username for the current user."""
    if request.user.is_authenticated:
        return request.user.display_name or request.user.username
    return 'anonymous'


def _get_avatar(request):
    """Return avatar for the current user."""
    if request.user.is_authenticated and request.user.avatar_url:
        return request.user.avatar_url
    return 'https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=100&q=80'


def _poll_annotation(poll, username):
    """Compute a poll's live totals + the given user's current selection.

    Returns (options, has_voted, selected_option_id, total_votes). Percentages
    are derived from actual PollVote rows so votes are per-user and re-votable.
    """
    total = poll.votes.count()
    sel = PollVote.objects.filter(poll=poll, user_name=username).values_list('option_id', flat=True).first()
    opts = list(poll.options.all())
    for o in opts:
        cnt = o.votes.count()
        o.percentage = round(cnt / total * 100) if total else 0
        o.is_selected = (sel is not None and o.id == sel)
    return opts, sel is not None, sel, total


def _annotate_posts(posts, request):
    """Add extra context to posts for the template."""
    username = _get_username(request)
    for post in posts:
        post.is_owner = post.author_name == username
        if post.post_type == 'poll' and hasattr(post, 'poll'):
            post.poll_obj = post.poll
            post.poll_options, post.poll_voted, post.poll_selected_id, post.poll_total = _poll_annotation(post.poll, username)
        else:
            post.poll_obj = None
            post.poll_options = []
            post.poll_voted = False
            post.poll_selected_id = None
            post.poll_total = 0


def _render_post_html(post, request):
    """Render a single post card as HTML string."""
    from django.template.loader import render_to_string
    # We use a small template snippet for individual posts
    return render_to_string(
        'dashboard/partials/community_post_card.html',
        {'post': post},
        request=request,
    )


def landing(request):
    return render(request, 'dashboard/pages/landing.html')


def _load_products():
    path = os.path.join(settings.BASE_DIR, 'dashboard', 'static', 'dashboard', 'js', 'products.js')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        match = re.search(r'window\.KAIMONO_PRODUCTS\s*=\s*(\[.*?\]);', text, re.DOTALL)
        if not match:
            return []
        raw = match.group(1)
        raw = re.sub(r'(?<=[\{,])\s*([A-Za-z_$][\w$]*)\s*:', r'"\1":', raw)
        raw = re.sub(r',\s*([}\]])', r'\1', raw)
        return json.loads(raw)
    except (OSError, ValueError):
        return []


def dashboard(request):
    products = _load_products()
    featured = [p for p in products if p.get('category') == 'games'][:3]
    discounts = sorted(
        (p for p in products if p.get('originalPrice')),
        key=lambda p: (p.get('originalPrice') or 0) - (p.get('price') or 0),
        reverse=True,
    )[:4]
    game_of_day = next(
        (p for p in products if p.get('category') == 'games' and p.get('originalPrice')),
        (products[0] if products else None),
    )
    context = {
        'today': timezone.now(),
        'featured': featured,
        'discounts': discounts,
        'game_of_day': game_of_day,
    }
    return render(request, 'dashboard/pages/dashboard.html', context)


def shop(request):
    products = [p.data for p in ShopProduct.objects.order_by('id') if p.data.get('active', True)]
    return render(request, 'dashboard/pages/shop.html', {
        'products_json': json.dumps(products),
    })


def _enrich_product_reviews(data):
    """Ensure every product has reviews, features, requirements, etc.

    Products from the hardcoded products.js (ids 1-12) get enriched client-side
    via the EXTRA map. This server-side helper fills in the same fields for
    products that were added through the admin panel or developer submissions
    so the game_detail page always has reviews to display.
    """
    import random as _random

    # Don't overwrite data that already exists (e.g. from EXTRA enrichment).
    if data.get('userReviews'):
        return data

    pid = data.get('id', 0)
    rng = _random.Random(pid)  # deterministic per product

    name = data.get('name', 'this game')
    category = data.get('category', 'games')
    is_game = category == 'games'

    # -- Review authors pool --
    authors = [
        ('gamer_pro', 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80'),
        ('pixel_ninja', 'https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80'),
        ('cosmic_rider', 'https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=80&q=80'),
        ('nova_star', 'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=80&q=80'),
        ('zen_player', 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80'),
        ('arcadia_x', 'https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=80&q=80'),
        ('blitz_runner', 'https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80'),
        ('echo_fox', 'https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=80&q=80'),
        ('drift_wave', 'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=80&q=80'),
        ('solar_knight', 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80'),
    ]

    # -- Positive review templates --
    pos_templates = [
        "Absolutely loving {name}! The gameplay is smooth and the experience has been fantastic.",
        "Picked up {name} on a whim and couldn't put it down. Highly recommend to anyone.",
        "One of the best {cat} experiences I've had in a long time. {name} delivers on every front.",
        "Bought {name} for a friend and they haven't stopped playing. Great value.",
        "The quality of {name} really surprised me. Way above my expectations.",
        "{name} has become one of my favorites. Great attention to detail and polish.",
        "Can't say enough good things about {name}. It's well worth the price.",
        "Finally got around to trying {name} — wish I had bought it sooner!",
    ]

    # -- Negative review templates --
    neg_templates = [
        "{name} has potential but the current state needs work. Waiting for patches.",
        "Was excited for {name} but it didn't quite hit the mark for me. Still decent though.",
        "{name} is okay — not bad, not amazing. It depends on what you're looking for.",
        "I wanted to love {name} more than I did. Some design choices held it back.",
        "Price feels a bit high for what {name} offers right now. Maybe wait for a sale.",
    ]

    langs = ['en', 'en', 'en', 'ja', 'es', 'de', 'fr', 'zh']
    num_reviews = rng.randint(4, 8)
    reviews = []
    for i in range(num_reviews):
        author_name, author_avatar = rng.choice(authors)
        positive = rng.random() < (0.75 if is_game else 0.8)
        templates = pos_templates if positive else neg_templates
        text = rng.choice(templates).format(name=name, cat=category)
        hours = round(rng.uniform(0.5, 200.0), 1) if is_game else None
        days_ago = rng.randint(1, 90)
        review_date = (datetime.date.today() - datetime.timedelta(days=days_ago)).isoformat()
        reviews.append({
            'author': author_name,
            'avatar': author_avatar,
            'date': review_date,
            'hours': hours,
            'lang': rng.choice(langs),
            'positive': positive,
            'text': text,
            'helpful': rng.randint(5, 150),
        })
    data['userReviews'] = reviews

    # reviewSummary
    if not data.get('reviewSummary'):
        pos_count = sum(1 for r in reviews if r['positive'])
        pct = pos_count / len(reviews) * 100 if reviews else 50
        if pct >= 95:
            data['reviewSummary'] = 'Overwhelmingly Positive'
        elif pct >= 80:
            data['reviewSummary'] = 'Very Positive'
        elif pct >= 60:
            data['reviewSummary'] = 'Positive'
        elif pct >= 40:
            data['reviewSummary'] = 'Mixed'
        else:
            data['reviewSummary'] = 'Mostly Negative'

    # metacritic
    if not data.get('metacritic'):
        data['metacritic'] = rng.randint(65, 96)

    # accolades
    if not data.get('accolades'):
        outlets = [
            ('IGN', '8.5'), ('GameSpot', '8/10'), ('PC Gamer', '85'),
            ('Eurogamer', 'Recommended'), ('Famitsu', '35/40'),
        ]
        chosen = rng.sample(outlets, k=min(3, len(outlets)))
        data['accolades'] = [
            {'outlet': o, 'score': s, 'quote': 'A solid experience that delivers on its promises.'}
            for o, s in chosen
        ]

    # about
    if not data.get('about'):
        desc = data.get('description', '') or f'{name} is a compelling {category} experience.'
        data['about'] = [desc]

    # keyFeatures
    if not data.get('keyFeatures'):
        tags = data.get('tags', [])
        if tags:
            data['keyFeatures'] = [f'{t} experience' for t in tags[:5]]
        else:
            data['keyFeatures'] = ['Engaging gameplay', 'High-quality production', 'Great value for money']

    # features (Steam-style)
    if not data.get('features'):
        if is_game:
            data['features'] = rng.sample(
                ['achievements', 'cloud', 'controller', 'singleplayer', 'multiplayer'],
                k=rng.randint(2, 4)
            )
        else:
            data['features'] = []

    # requirements (games only)
    if is_game and not data.get('requirements'):
        data['requirements'] = {
            'minimum': {
                'os': 'Windows 10 64-bit',
                'cpu': 'Intel Core i5 / AMD Ryzen 5',
                'ram': '8 GB RAM',
                'gpu': 'NVIDIA GTX 1060 / AMD RX 580',
                'directx': 'DirectX 12',
                'storage': '50 GB available space',
            },
            'recommended': {
                'os': 'Windows 11 64-bit',
                'cpu': 'Intel Core i7 / AMD Ryzen 7',
                'ram': '16 GB RAM',
                'gpu': 'NVIDIA RTX 3060 / AMD RX 6600',
                'directx': 'DirectX 12',
                'storage': '50 GB SSD',
            },
        }

    return data


def game_detail(request, product_id):
    product = None
    try:
        candidate = ShopProduct.objects.get(id=int(product_id))
        if candidate.data.get('active', True):
            product = candidate.data
    except (ShopProduct.DoesNotExist, ValueError):
        product = None
    if product:
        product = _enrich_product_reviews(product)
    return render(request, 'dashboard/pages/game_detail.html', {
        'product_id': product_id,
        'product_json': json.dumps([product]) if product else '[]',
    })


def checkout_complete(request):
    """Create library entries when a user completes checkout (games only)."""
    if not request.user.is_authenticated:
        return JsonResponse({'ok': False, 'detail': 'login'}, status=401)
    try:
        body = json.loads(request.body)
    except (ValueError, TypeError):
        body = {}
    ids = body.get('product_ids') or []
    if isinstance(ids, int):
        ids = [ids]

    added = 0
    skipped = 0
    for pid in ids:
        try:
            sp = ShopProduct.objects.get(id=int(pid))
        except (ShopProduct.DoesNotExist, ValueError):
            continue
        if sp.category != 'games':
            skipped += 1
            continue
        if request.user.library_games.filter(title=sp.name).exists():
            continue
        LibraryGame.objects.create(
            user=request.user,
            title=sp.name,
            studio=sp.data.get('brand', ''),
            image_url=sp.image or sp.data.get('image', ''),
            meta='',
            status='Not Installed',
            badge='',
            favorite=False,
        )
        added += 1
    return JsonResponse({'ok': True, 'added': added, 'skipped': skipped})


def community(request):
    stories = list(CommunityStory.objects.all())
    channels = list(CommunityChannel.objects.filter(is_active=True))

    username = _get_username(request)
    followed_fos = list(
        UserFollowedGame.objects.select_related('game').filter(user_name=username)
    )
    followed_game_ids = {f.game_id for f in followed_fos}
    games = [f.game for f in followed_fos]
    friends = list(CommunityMember.objects.all())

    # Feed filter
    feed_filter = request.GET.get('feed', 'for-you')
    channel_filter = request.GET.get('channel', '')
    search_query = request.GET.get('q', '').strip()

    posts_qs = CommunityPost.objects.select_related().prefetch_related(
        'images', 'tags', 'reaction_types', 'poll', 'poll__options',
    )

    # Channel filter
    if channel_filter:
        posts_qs = posts_qs.filter(channel__slug=channel_filter)

    # Search filter
    if search_query:
        posts_qs = posts_qs.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author_name__icontains=search_query)
        )

    # Feed type filter
    if feed_filter == 'trending':
        posts_qs = posts_qs.order_by('-reaction_count', '-created_at')
    elif feed_filter == 'latest':
        posts_qs = posts_qs.order_by('-created_at')
    elif feed_filter == 'media':
        posts_qs = posts_qs.filter(post_type='image')
    elif feed_filter == 'following':
        # Show all for now (would need follow model)
        pass
    else:  # for-you
        posts_qs = posts_qs.order_by('-is_pinned', '-created_at')

    total_posts_count = posts_qs.count()
    page = int(request.GET.get('page', 1))
    total_pages = math.ceil(total_posts_count / POSTS_PER_PAGE)
    posts = list(posts_qs[(page - 1) * POSTS_PER_PAGE: page * POSTS_PER_PAGE])

    _annotate_posts(posts, request)

    total_members = sum(ch.post_count for ch in channels)

    # If AJAX request, return just the post HTML (load-more via page, feed/channel switch, or All/plain)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posts_html = ''
        for post in posts:
            posts_html += _render_post_html(post, request)
        return JsonResponse({
            'posts_html': posts_html,
            'has_next': page < total_pages,
            'total_posts': total_posts_count,
        })

    ctx = {
        'stories': stories,
        'channels': channels,
        'games': games,
        'friends': friends,
        'followed_game_ids': followed_game_ids,
        'posts': posts,
        'total_members': total_members,
        'current_feed': feed_filter,
        'current_channel': channel_filter,
        'search_query': search_query,
        'has_next': page < total_pages,
        'total_pages': total_pages,
        'current_page': page,
    }
    return render(request, 'dashboard/pages/community.html', ctx)


# ── AJAX: Vote Poll ───────────────────────────────────────────────

@require_POST
def community_vote_poll(request):
    try:
        data = json.loads(request.body)
        option_id = int(data.get('option_id'))
        option = PollOption.objects.select_related('poll').get(id=option_id)
    except (PollOption.DoesNotExist, TypeError, ValueError, KeyError):
        return JsonResponse({'error': 'Option not found'}, status=404)
    poll = option.poll
    username = _get_username(request)

    # Per-user vote: move the current user's vote to the chosen option.
    existing = PollVote.objects.filter(poll=poll, user_name=username).first()
    if existing is None or existing.option_id != option_id:
        if existing is not None:
            existing.delete()
        PollVote.objects.create(poll=poll, option=option, user_name=username)

    opts, voted, sel, total = _poll_annotation(poll, username)
    return JsonResponse({
        'voted': True,
        'total_votes': total,
        'poll_voted': voted,
        'selected_option_id': sel,
        'options': [
            {'id': o.id, 'label': o.label, 'percentage': o.percentage, 'is_selected': o.is_selected}
            for o in opts
        ],
    })


# ── AJAX: Create Post ─────────────────────────────────────────────

@require_POST
def community_create_post(request):
    try:
        data = json.loads(request.body)
        post_type = data.get('post_type', 'discussion')
        title = data.get('title', '')
        content = data.get('content', '')
        channel_slug = data.get('channel', '')
        image_urls = data.get('image_urls', [])

        if post_type == 'poll':
            if not data.get('poll_question'):
                return JsonResponse({'error': 'Poll question is required'}, status=400)
        elif not content and not title:
            return JsonResponse({'error': 'Content or title is required'}, status=400)

        channel = None
        if channel_slug:
            channel = CommunityChannel.objects.filter(slug=channel_slug).first()

        post = CommunityPost.objects.create(
            post_type=post_type,
            title=title,
            content=content,
            author_name=_get_username(request),
            author_avatar=_get_avatar(request),
            channel=channel,
            time_ago='Just now',
            visibility='Public',
        )

        # Add images
        for i, url in enumerate(image_urls):
            if url.strip():
                PostImage.objects.create(post=post, url=url.strip(), order=i)

        # Add tags from content (#hashtags)
        import re
        tags = re.findall(r'#(\w+)', content)
        for tag_name in tags:
            PostTag.objects.create(post=post, name=tag_name)

        # Update channel post count
        if channel:
            channel.post_count += 1
            channel.save(update_fields=['post_count'])

        # Create poll if poll type
        poll_question = data.get('poll_question', '')
        poll_options_list = data.get('poll_options', [])
        if post_type == 'poll' and poll_question and len(poll_options_list) >= 2:
            from .models import Poll as PollModel, PollOption as PollOptionModel
            poll = PollModel.objects.create(
                post=post,
                question=poll_question,
                total_votes=0,
                time_left='7 days left',
            )
            for i, label in enumerate(poll_options_list[:6]):
                PollOptionModel.objects.create(poll=poll, label=label, percentage=0, order=i)

        # Return the rendered post card
        if post.post_type == 'poll' and hasattr(post, 'poll'):
            post.poll_obj = post.poll
            post.poll_options, post.poll_voted, post.poll_selected_id, post.poll_total = _poll_annotation(post.poll, _get_username(request))
        else:
            post.poll_obj = None
            post.poll_options = []
            post.poll_voted = False
            post.poll_selected_id = None
            post.poll_total = 0
        html = _render_post_html(post, request)

        return JsonResponse({'success': True, 'post_html': html, 'post_id': post.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# ── AJAX: Edit Post ───────────────────────────────────────────────

@require_POST
def community_edit_post(request):
    try:
        data = json.loads(request.body)
        post_id = data.get('post_id')
        post = CommunityPost.objects.get(id=post_id)
        username = _get_username(request)

        if post.author_name != username:
            return JsonResponse({'error': 'Not authorized to edit this post'}, status=403)

        title = data.get('title', '').strip()
        content = data.get('content', '').strip()

        if post.post_type == 'poll':
            if not title:
                return JsonResponse({'error': 'Poll question is required'}, status=400)
            post.title = title
            if hasattr(post, 'poll'):
                post.poll.question = title
                post.poll.save(update_fields=['question'])
        else:
            post.title = title
            post.content = content

        post.time_ago = 'Edited just now'
        post.save(update_fields=['title', 'content', 'time_ago'])

        if post.post_type == 'poll' and hasattr(post, 'poll'):
            post.poll_obj = post.poll
            post.poll_options, post.poll_voted, post.poll_selected_id, post.poll_total = _poll_annotation(post.poll, username)
        else:
            post.poll_obj = None
            post.poll_options = []
            post.poll_voted = False
            post.poll_selected_id = None
            post.poll_total = 0

        post.is_owner = post.author_name == username

        return JsonResponse({'success': True, 'post_html': _render_post_html(post, request)})
    except CommunityPost.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# ── AJAX: Delete Post ─────────────────────────────────────────────

@require_POST
def community_delete_post(request):
    try:
        data = json.loads(request.body)
        post_id = data.get('post_id')
        post = CommunityPost.objects.get(id=post_id)
        username = _get_username(request)

        if post.author_name != username:
            return JsonResponse({'error': 'Not authorized to delete this post'}, status=403)

        channel = post.channel
        post.delete()
        if channel:
            channel.post_count = max(0, channel.post_count - 1)
            channel.save(update_fields=['post_count'])

        return JsonResponse({'success': True, 'post_id': post_id})
    except CommunityPost.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# ── AJAX: Add Comment ─────────────────────────────────────────────

@require_POST
def community_add_comment(request):
    try:
        data = json.loads(request.body)
        post_id = data.get('post_id')
        content = data.get('content', '').strip()

        if not content:
            return JsonResponse({'error': 'Content is required'}, status=400)

        post = CommunityPost.objects.get(id=post_id)

        comment = CommunityComment.objects.create(
            post=post,
            author_name=_get_username(request),
            author_avatar=_get_avatar(request),
            content=content,
        )

        # Update counter
        post.comment_count += 1
        post.save(update_fields=['comment_count'])

        return JsonResponse({
            'success': True,
            'comment': {
                'id': comment.id,
                'author_name': comment.author_name,
                'author_avatar': comment.author_avatar,
                'content': comment.content,
                'created_at': 'Just now',
            },
            'total_comments': post.comment_count,
        })
    except CommunityPost.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# ── AJAX: Get Comments ────────────────────────────────────────────

@require_GET
def community_get_comments(request):
    try:
        post_id = request.GET.get('post_id')
        comments = CommunityComment.objects.filter(post_id=post_id)
        data = [{
            'id': c.id,
            'author_name': c.author_name,
            'author_avatar': c.author_avatar,
            'content': c.content,
            'created_at': 'Just now',
        } for c in comments]
        return JsonResponse({'comments': data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# ── AJAX: Share Post (increment counter) ──────────────────────────

@require_POST
def community_share_post(request):
    try:
        data = json.loads(request.body)
        post_id = data.get('post_id')
        post = CommunityPost.objects.get(id=post_id)
        post.share_count += 1
        post.save(update_fields=['share_count'])
        return JsonResponse({'success': True, 'count': post.share_count})
    except CommunityPost.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# ── AJAX: Follow / Unfollow a community game ───────────────────────

@require_POST
def community_toggle_follow_game(request):
    try:
        data = json.loads(request.body)
    except (ValueError, TypeError):
        data = {}
    username = _get_username(request)

    game_id = data.get('game_id')
    name = (data.get('name') or '').strip()
    if not game_id and name:
        game, _ = CommunityGame.objects.get_or_create(
            name=name,
            defaults={'image_url': data.get('image', '') or ''},
        )
        game_id = game.id
    if not game_id:
        return JsonResponse({'error': 'Game is required.'}, status=400)

    try:
        game = CommunityGame.objects.get(id=game_id)
    except CommunityGame.DoesNotExist:
        return JsonResponse({'error': 'Game not found.'}, status=404)

    follow, created = UserFollowedGame.objects.get_or_create(
        user_name=username, game=game
    )
    # Honor an explicit desired state (sent from game detail), else toggle.
    wanted = data.get('followed')
    if wanted is None:
        if not created:
            follow.delete()
    elif wanted is True:
        pass  # already followed (created True) or existing
    else:
        if not created:
            follow.delete()
    is_followed = UserFollowedGame.objects.filter(
        user_name=username, game=game
    ).exists()
    count = UserFollowedGame.objects.filter(user_name=username).count()
    return JsonResponse({'followed': is_followed, 'count': count})

# ── Admin Panel ─────────────────────────────────────────────────────

def _admin_required(view_func):
    """Login + staff-only gate for admin panel routes."""
    from django.contrib.auth.decorators import login_required
    from django.core.exceptions import PermissionDenied

    @login_required
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("Admin access only")
        return view_func(request, *args, **kwargs)
    return _wrapped


def _admin_section(request):
    """Current admin tab, e.g. products, users, community, submissions."""
    section = request.GET.get("section") or request.POST.get("section") or "overview"
    if section not in ("overview", "products", "users", "community", "submissions"):
        section = "overview"
    return section


def _build_admin_context(request, section):
    products = list(ShopProduct.objects.order_by("id"))
    posts = list(CommunityPost.objects.select_related("channel").order_by("-created_at"))
    comments = list(CommunityComment.objects.select_related("post").order_by("-created_at"))
    submissions = list(GameSubmission.objects.select_related('developer').order_by('-created_at'))
    pending_subs = [s for s in submissions if s.status == 'pending']
    return {
        "section": section,
        "products": products,
        "products_count": len(products),
        "active_products_count": sum(1 for p in products if p.data.get("active", True)),
        "users": list(User.objects.order_by("-date_joined")),
        "users_count": User.objects.count(),
        "staff_count": User.objects.filter(is_staff=True).count(),
        "posts": posts,
        "posts_count": len(posts),
        "channels": list(CommunityChannel.objects.order_by("name")),
        "channels_count": CommunityChannel.objects.count(),
        "comments": comments,
        "comments_count": len(comments),
        "members": list(CommunityMember.objects.all()),
        "members_count": CommunityMember.objects.count(),
        "library_count": LibraryGame.objects.count(),
        "wishlist_count": WishlistItem.objects.count(),
        "recent_posts": posts[:5],
        "recent_users": list(User.objects.all().order_by("-date_joined")[:5]),
        "submissions": submissions,
        "submissions_count": len(submissions),
        "pending_submissions_count": len(pending_subs),
    }


@_admin_required
def admin_panel(request):
    section = _admin_section(request)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "product_save":
            return _admin_product_save(request)
        if action == "product_delete":
            pid = request.POST.get("id")
            ShopProduct.objects.filter(id=pid).delete()
            messages.success(request, "Product deleted.")
            return redirect(reverse("admin_panel") + "?section=products")
        if action == "product_toggle":
            try:
                p = ShopProduct.objects.get(id=request.POST.get("id"))
                p.data = dict(p.data)
                p.data["active"] = not p.data.get("active", True)
                p.save(update_fields=["data"])
                messages.success(request, "Product visibility updated.")
            except ShopProduct.DoesNotExist:
                messages.error(request, "Product not found.")
            return redirect(reverse("admin_panel") + "?section=products")
        if action == "user_save":
            return _admin_user_save(request)
        if action == "user_delete":
            try:
                target = User.objects.get(id=request.POST.get("id"))
                if target.pk == request.user.pk:
                    messages.error(request, "You cannot delete your own account.")
                else:
                    target.delete()
                    messages.success(request, "User deleted.")
            except User.DoesNotExist:
                messages.error(request, "User not found.")
            return redirect(reverse("admin_panel") + "?section=users")
        if action == "user_toggle":
            try:
                target = User.objects.get(id=request.POST.get("id"))
                if target.pk == request.user.pk:
                    messages.error(request, "You cannot change your own admin status.")
                else:
                    target.is_staff = not target.is_staff
                    target.save(update_fields=["is_staff"])
                    messages.success(request, "Admin status updated.")
            except User.DoesNotExist:
                messages.error(request, "User not found.")
            return redirect(reverse("admin_panel") + "?section=users")
        if action == "channel_save":
            return _admin_channel_save(request)
        if action == "channel_toggle":
            ch = CommunityChannel.objects.filter(id=request.POST.get("id")).first()
            if ch:
                ch.is_active = not ch.is_active
                ch.save(update_fields=["is_active"])
                messages.success(request, "Channel updated.")
            return redirect(reverse("admin_panel") + "?section=community")
        if action == "channel_delete":
            CommunityChannel.objects.filter(id=request.POST.get("id")).delete()
            messages.success(request, "Channel deleted.")
            return redirect(reverse("admin_panel") + "?section=community")
        if action == "post_delete":
            try:
                post = CommunityPost.objects.get(id=request.POST.get("id"))
                channel = post.channel
                post.delete()
                if channel:
                    channel.post_count = max(0, channel.post_count - 1)
                    channel.save(update_fields=["post_count"])
                messages.success(request, "Post deleted.")
            except CommunityPost.DoesNotExist:
                messages.error(request, "Post not found.")
            return redirect(reverse("admin_panel") + "?section=community")
        if action == "post_pin":
            post = CommunityPost.objects.filter(id=request.POST.get("id")).first()
            if post:
                post.is_pinned = not post.is_pinned
                post.save(update_fields=["is_pinned"])
                messages.success(request, "Pin updated.")
            return redirect(reverse("admin_panel") + "?section=community")
        if action == "comment_delete":
            CommunityComment.objects.filter(id=request.POST.get("id")).delete()
            return redirect(reverse("admin_panel") + "?section=community")
        if action == "member_save":
            return _admin_member_save(request)
        if action == "member_delete":
            CommunityMember.objects.filter(id=request.POST.get("id")).delete()
            messages.success(request, "Member removed.")
            return redirect(reverse("admin_panel") + "?section=community")
        if action == "submission_accept":
            return _admin_submission_accept(request)
        if action == "submission_reject":
            return _admin_submission_reject(request)
        messages.error(request, "Unknown action.")
        return redirect(reverse("admin_panel") + f"?section={section}")

    ctx = _build_admin_context(request, section)
    # Prefill the product/user create+edit form.
    if section == "products":
        edit_id = request.GET.get("edit")
        product = None
        if edit_id:
            product = ShopProduct.objects.filter(id=edit_id).first()
        ctx["product_form"] = _admin_product_form(product)
        ctx["edit_product_id"] = product.pk if product else None
        ctx["edit_screenshots"] = (product.data or {}).get("screenshots", []) if product else []
    elif section == "users":
        edit_id = request.GET.get("edit")
        edit_user = None
        if edit_id:
            edit_user = User.objects.filter(id=edit_id).first()
        ctx["user_form"] = AdminUserForm(instance=edit_user)
        ctx["edit_user_id"] = edit_user.pk if edit_user else None
    elif section == "community":
        ctx["channel_form"] = AdminChannelForm()
        ctx["member_form"] = AdminMemberForm()
    return render(request, "dashboard/pages/admin_panel.html", ctx)


def _admin_product_save(request):
    form = AdminProductForm(request.POST, request.FILES)
    if not form.is_valid():
        for field in form.errors.values():
            for err in field:
                messages.error(request, f"{err}")
        return redirect(reverse("admin_panel") + "?section=products")

    pid = request.POST.get("id")
    product = ShopProduct.objects.filter(id=pid).first() if pid else None

    from accounts import storage

    # If a new image file was uploaded, push it to Supabase Storage and use its
    # public URL. Otherwise keep the posted URL (or the product's existing one).
    uploaded = form.cleaned_data.get("image_file")
    image_url = form.cleaned_data.get("image", "").strip()
    if uploaded:
        image_url = storage.upload_image(uploaded, folder="products") or image_url

    data = form.build_data(product.id if product else None)
    data["image"] = image_url
    if not image_url and product:
        data["image"] = (product.data or {}).get("image", "")

    # Multi-image screenshots: any newly uploaded files are pushed to storage and
    # appended; otherwise the product's current screenshots are preserved.
    shot_files = form.cleaned_data.get("screenshot_files") or []
    if shot_files:
        screenshots = []
        for f in shot_files:
            url = storage.upload_image(f, folder="products")
            if url:
                screenshots.append(url)
        data["screenshots"] = screenshots
    elif product and (product.data or {}).get("screenshots"):
        data["screenshots"] = (product.data or {}).get("screenshots", [])
    elif data["image"] and not data["screenshots"]:
        data["screenshots"] = [data["image"]]

    if product:
        # Preserve extras (friends, bundles) unless being edited away. Media is
        # rebuilt via the form so the trailer (if provided) goes first.
        old = product.data or {}
        data["media"] = form.build_media(old.get("media", []))
        data["friends"] = old.get("friends", [])
        data["bundles"] = old.get("bundles", [])
        product.name = data["name"]
        product.category = data["category"]
        product.price = data.get("price")
        product.original_price = data.get("originalPrice")
        product.image = data.get("image") or ""
        product.data = data
        product.save()
        messages.success(request, "Product updated.")
    else:
        data["media"] = form.build_media([])
        product = ShopProduct.objects.create(
            name=data["name"],
            category=data["category"],
            price=data.get("price"),
            original_price=data.get("originalPrice"),
            image=data.get("image") or "",
            data=data,
        )
        # Keep data['id'] in sync with the real DB id (shop/cart/checkout depend on it).
        product.data = dict(product.data)
        product.data["id"] = product.id
        product.save(update_fields=["data"])
        messages.success(request, "Product created.")
    return redirect(reverse("admin_panel") + "?section=products")


def _admin_user_save(request):
    form = AdminUserForm(request.POST)
    if not form.is_valid():
        for err in form.errors.values():
            for msg in err:
                messages.error(request, f"{msg}")
        return redirect(request.POST.get("next") or (reverse("admin_panel") + "?section=users"))
    user = form.save()
    messages.success(request, "User saved.")
    return redirect(reverse("admin_panel") + "?section=users")


def _admin_channel_save(request):
    form = AdminChannelForm(request.POST)
    if not form.is_valid():
        for err in form.errors.values():
            for msg in err:
                messages.error(request, f"{msg}")
        return redirect(reverse("admin_panel") + "?section=community")
    channel, created = CommunityChannel.objects.update_or_create(
        id=request.POST.get("id") or None,
        defaults=form.cleaned_data,
    )
    messages.success(request, "Channel saved.")
    return redirect(reverse("admin_panel") + "?section=community")


def _admin_member_save(request):
    form = AdminMemberForm(request.POST)
    if not form.is_valid():
        for err in form.errors.values():
            for msg in err:
                messages.error(request, f"{msg}")
        return redirect(reverse("admin_panel") + "?section=community")
    cd = form.cleaned_data
    member_id = request.POST.get("id")
    if member_id:
        member = CommunityMember.objects.filter(id=member_id).first()
        if member:
            for k, v in cd.items():
                setattr(member, k, v)
            member.save()
    else:
        CommunityMember.objects.create(
            **cd,
            last_active="Just now",
            level=1,
            games_played=0,
            achievements=0,
            followers=0,
            member_since="",
        )
    messages.success(request, "Member saved.")
    return redirect(reverse("admin_panel") + "?section=community")


def _admin_submission_accept(request):
    """Accept a game submission: create a ShopProduct and mark as accepted."""
    try:
        sub = GameSubmission.objects.get(id=request.POST.get('id'))
    except GameSubmission.DoesNotExist:
        messages.error(request, "Submission not found.")
        return redirect(reverse('admin_panel') + '?section=submissions')

    data = sub.to_product_data()
    product = ShopProduct.objects.create(
        name=sub.name,
        category=sub.category,
        price=sub.price,
        original_price=sub.original_price,
        image=sub.image,
        data=data,
    )
    # Keep data['id'] in sync with the real DB id
    data['id'] = product.id
    product.data = data
    product.save(update_fields=['data'])

    sub.status = 'accepted'
    sub.admin_note = request.POST.get('note', '').strip()
    sub.save(update_fields=['status', 'admin_note', 'reviewed_at'])

    messages.success(request, f"'{sub.name}' accepted and added to the shop!")
    return redirect(reverse('admin_panel') + '?section=submissions')


def _admin_submission_reject(request):
    """Reject a game submission with an optional admin note."""
    try:
        sub = GameSubmission.objects.get(id=request.POST.get('id'))
    except GameSubmission.DoesNotExist:
        messages.error(request, "Submission not found.")
        return redirect(reverse('admin_panel') + '?section=submissions')

    sub.status = 'rejected'
    sub.admin_note = request.POST.get('note', '').strip()
    sub.save(update_fields=['status', 'admin_note', 'reviewed_at'])

    messages.success(request, f"'{sub.name}' rejected.")
    return redirect(reverse('admin_panel') + '?section=submissions')


def _admin_product_form(product):
    """Return a bound AdminProductForm for editing an existing product."""
    from .forms import AdminProductForm
    if not product:
        return AdminProductForm()
    d = product.data or {}
    initial = {
        "name": product.name,
        "category": product.category,
        "brand": d.get("brand", ""),
        "type": d.get("type", ""),
        "price": product.price,
        "original_price": product.original_price,
        "stock": d.get("stock", ""),
        "badges": ", ".join(d.get("badges", [])),
        "rating": d.get("rating"),
        "reviews": d.get("reviews"),
        "popularity": d.get("popularity"),
        "image": product.image or d.get("image", ""),
        "description": d.get("description", ""),
        "developer": d.get("developer", ""),
        "publisher": d.get("publisher", ""),
        "release_date": d.get("releaseDate", ""),
        "tags": ", ".join(d.get("tags", [])),
        "is_active": d.get("active", True),
        "trailer_url": next((m.get("url", "") or m.get("src", "") for m in (d.get("media") or []) if m.get("youtube")), ""),
    }
    return AdminProductForm(initial=initial)


def developer_panel(request):
    """Developer panel: submit games for admin review."""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role != 'developer':
        messages.error(request, "Developer access only.")
        return redirect('settings')

    my_submissions = list(
        GameSubmission.objects.filter(developer=request.user).order_by('-created_at')
    )
    ctx = {
        'submissions': my_submissions,
        'pending_count': sum(1 for s in my_submissions if s.status == 'pending'),
        'accepted_count': sum(1 for s in my_submissions if s.status == 'accepted'),
        'rejected_count': sum(1 for s in my_submissions if s.status == 'rejected'),
    }
    return render(request, 'dashboard/pages/developer_panel.html', ctx)


def developer_panel_submit(request):
    """Handle game submission POST from the developer panel."""
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role != 'developer':
        messages.error(request, "Developer access only.")
        return redirect('settings')

    if request.method != 'POST':
        return redirect('developer_panel')

    name = request.POST.get('name', '').strip()
    if not name:
        messages.error(request, "Game title is required.")
        return redirect('developer_panel')

    # Handle image upload via Supabase storage
    image_url = request.POST.get('image', '').strip()
    uploaded = request.FILES.get('image_file')
    if uploaded:
        from accounts import storage
        image_url = storage.upload_image(uploaded, folder='submissions') or image_url

    # Handle screenshot uploads
    screenshots = []
    screenshot_files = request.FILES.getlist('screenshot_files')
    if screenshot_files:
        from accounts import storage
        for f in screenshot_files:
            url = storage.upload_image(f, folder='submissions')
            if url:
                screenshots.append(url)

    GameSubmission.objects.create(
        developer=request.user,
        name=name,
        category='games',
        type=request.POST.get('type', '').strip(),
        brand=request.POST.get('brand', '').strip(),
        price=request.POST.get('price') or None,
        original_price=request.POST.get('original_price') or None,
        image=image_url,
        description=request.POST.get('description', '').strip(),
        tags=request.POST.get('tags', '').strip(),
        trailer_url=request.POST.get('trailer_url', '').strip(),
        stock=request.POST.get('stock', 'In Stock').strip(),
        badges=request.POST.get('badges', '').strip(),
        developer_name=request.POST.get('developer_name', '').strip(),
        publisher=request.POST.get('publisher', '').strip(),
        release_date=request.POST.get('release_date', '').strip(),
        screenshots=screenshots,
    )
    messages.success(request, f"'{name}' submitted for review!")
    return redirect('developer_panel')


# ── Wishlist ────────────────────────────────────────────────────────

@login_required
def wishlist(request):
    items = list(
        UserWishlistItem.objects.filter(user=request.user)
        .select_related('product')
        .order_by('-created_at')
    )
    products = [wi.product for wi in items]
    on_sale = [p for p in products if p.original_price and p.price and p.original_price > p.price]
    total_value = sum((p.price or 0) for p in products if p.price)
    savings = sum(((p.original_price or 0) - (p.price or 0)) for p in on_sale)
    games = [p for p in products if p.category == 'games']
    merch = [p for p in products if p.category != 'games']
    bundles = []
    # Build product data list for the template
    product_data = []
    for wi in items:
        p = wi.product
        d = p.data or {}
        product_data.append({
            'id': p.id,
            'wishlist_id': wi.id,
            'name': p.name,
            'category': p.category,
            'image': p.image or d.get('image', ''),
            'brand': d.get('brand', ''),
            'type': d.get('type', ''),
            'price': float(p.price) if p.price else 0,
            'original_price': float(p.original_price) if p.original_price else None,
            'rating': d.get('rating', 0),
            'reviews': d.get('reviews', 0),
            'badges': d.get('badges', []),
            'stock': d.get('stock', ''),
            'description': d.get('description', ''),
        })
    ctx = {
        "products_json": json.dumps(product_data),
        "items": product_data,
        "total_count": len(product_data),
        "on_sale_count": len(on_sale),
        "total_value": total_value,
        "savings": savings,
        "games_count": len(games),
        "merch_count": len(merch),
        "bundles_count": len(bundles),
    }
    return render(request, 'dashboard/pages/wishlist.html', ctx)


# ── AJAX: Toggle Wishlist ────────────────────────────────────────

@require_POST
def api_wishlist_toggle(request):
    """Add or remove a product from the current user's wishlist."""
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=401)
    try:
        data = json.loads(request.body)
        product_id = int(data.get('product_id'))
    except (ValueError, TypeError, KeyError):
        return JsonResponse({'error': 'Invalid product_id'}, status=400)

    try:
        product = ShopProduct.objects.get(id=product_id)
    except ShopProduct.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    item, created = UserWishlistItem.objects.get_or_create(
        user=request.user, product=product,
    )
    if not created:
        item.delete()
        wished = False
    else:
        wished = True

    count = UserWishlistItem.objects.filter(user=request.user).count()
    return JsonResponse({'wished': wished, 'count': count})


@require_GET
def api_wishlist_list(request):
    """Return the current user's wishlist product IDs."""
    if not request.user.is_authenticated:
        return JsonResponse({'product_ids': [], 'count': 0})
    ids = list(
        UserWishlistItem.objects.filter(user=request.user)
        .values_list('product_id', flat=True)
    )
    return JsonResponse({'product_ids': ids, 'count': len(ids)})


# ── AJAX: Game Reviews ─────────────────────────────────────────────

@require_GET
def api_game_reviews(request):
    """Return user-submitted reviews for a product, plus the server-enriched reviews."""
    product_id = request.GET.get('product_id')
    if not product_id:
        return JsonResponse({'error': 'product_id required'}, status=400)
    try:
        product = ShopProduct.objects.get(id=int(product_id))
    except (ShopProduct.DoesNotExist, ValueError):
        return JsonResponse({'error': 'Product not found'}, status=404)

    # Server-enriched reviews from product data (seed data)
    seed_reviews = (product.data or {}).get('userReviews', [])
    # User-submitted reviews from DB
    db_reviews = [r.to_dict() for r in product.reviews.all()]
    # Combine: seed first, then user reviews (newest first)
    all_reviews = seed_reviews + db_reviews
    pos = sum(1 for r in all_reviews if r.get('positive'))
    pct = round(pos / len(all_reviews) * 100) if all_reviews else 0
    return JsonResponse({
        'reviews': all_reviews,
        'total': len(all_reviews),
        'positive_pct': pct,
        'summary': (product.data or {}).get('reviewSummary', ''),
    })


@require_POST
def api_game_review_submit(request):
    """Submit a user review for a product."""
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=401)
    try:
        body = json.loads(request.body)
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    product_id = body.get('product_id')
    text = (body.get('text') or '').strip()
    positive = body.get('positive')
    lang = (body.get('lang') or 'en').strip()[:10]
    hours = body.get('hours')

    if not product_id:
        return JsonResponse({'error': 'product_id required'}, status=400)
    if not text:
        return JsonResponse({'error': 'Review text is required'}, status=400)
    if positive is None:
        return JsonResponse({'error': 'Verdict (positive) is required'}, status=400)

    try:
        product = ShopProduct.objects.get(id=int(product_id))
    except (ShopProduct.DoesNotExist, ValueError):
        return JsonResponse({'error': 'Product not found'}, status=404)

    review = GameReview.objects.create(
        product=product,
        author_name=request.user.display_name or request.user.username,
        author_avatar=request.user.avatar_url or '',
        positive=bool(positive),
        text=text,
        lang=lang,
        hours=float(hours) if hours is not None else None,
    )
    return JsonResponse({'success': True, 'review': review.to_dict()})


def library(request):
    if request.user.is_authenticated:
        games = list(request.user.library_games.all().order_by('created_at'))
    else:
        games = list(LibraryGame.objects.all().order_by('created_at'))
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