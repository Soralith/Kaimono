import json
import math
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.db.models import Q
from .models import (
    WishlistItem, LibraryGame,
    CommunityStory, CommunityChannel, CommunityGame, CommunityPost,
    PostImage, PostTag, PostReaction, Poll, PollOption,
    CommunityComment, UserLike, UserBookmark,
    CommunityMember, UserFollowedGame,
)

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


def _annotate_posts(posts, request):
    """Add extra context to posts for the template."""
    username = _get_username(request)
    liked_ids = set(
        UserLike.objects.filter(user_name=username).values_list('post_id', flat=True)
    )
    bookmarked_ids = set(
        UserBookmark.objects.filter(user_name=username).values_list('post_id', flat=True)
    )
    for post in posts:
        post.reactions = list(post.reaction_types.all())
        post.is_liked = post.id in liked_ids
        post.is_bookmarked = post.id in bookmarked_ids
        if post.post_type == 'poll' and hasattr(post, 'poll'):
            post.poll_obj = post.poll
            post.poll_options = list(post.poll.options.all())
        else:
            post.poll_obj = None
            post.poll_options = []


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


# ── AJAX: Toggle Like ─────────────────────────────────────────────

@require_POST
def community_toggle_like(request):
    try:
        data = json.loads(request.body)
        post_id = data.get('post_id')
        post = CommunityPost.objects.get(id=post_id)
        username = _get_username(request)

        like, created = UserLike.objects.get_or_create(
            user_name=username, post=post
        )
        if not created:
            like.delete()
            post.reaction_count = max(0, post.reaction_count - 1)
            post.save(update_fields=['reaction_count'])
            return JsonResponse({'liked': False, 'count': post.reaction_count})
        else:
            post.reaction_count += 1
            post.save(update_fields=['reaction_count'])
            return JsonResponse({'liked': True, 'count': post.reaction_count})
    except CommunityPost.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# ── AJAX: Toggle Bookmark ─────────────────────────────────────────

@require_POST
def community_toggle_bookmark(request):
    try:
        data = json.loads(request.body)
        post_id = data.get('post_id')
        post = CommunityPost.objects.get(id=post_id)
        username = _get_username(request)

        bm, created = UserBookmark.objects.get_or_create(
            user_name=username, post=post
        )
        if not created:
            bm.delete()
            post.bookmark_count = max(0, post.bookmark_count - 1)
            post.save(update_fields=['bookmark_count'])
            return JsonResponse({'bookmarked': False, 'count': post.bookmark_count})
        else:
            post.bookmark_count += 1
            post.save(update_fields=['bookmark_count'])
            return JsonResponse({'bookmarked': True, 'count': post.bookmark_count})
    except CommunityPost.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# ── AJAX: Vote Poll ───────────────────────────────────────────────

@require_POST
def community_vote_poll(request):
    try:
        data = json.loads(request.body)
        option_id = data.get('option_id')
        option = PollOption.objects.select_related('poll').get(id=option_id)
        poll = option.poll

        # Mark selected
        if not option.is_selected:
            poll.options.filter(is_selected=True).update(is_selected=False)
            option.is_selected = True
            option.save(update_fields=['is_selected'])

            poll.total_votes += 1
            poll.save(update_fields=['total_votes'])

            # Simple percentage bump: voted option gets +15%, others share -15%
            opts = list(poll.options.all())
            n = len(opts)
            if n > 0:
                bump = 15
                share = bump // max(1, n - 1) if n > 1 else 0
                for o in opts:
                    if o.is_selected:
                        o.percentage = min(95, o.percentage + bump)
                    else:
                        o.percentage = max(1, o.percentage - share)
                # Normalize to 100
                total_pct = sum(o.percentage for o in opts)
                if total_pct != 100 and opts:
                    opts[0].percentage += 100 - total_pct
                PollOption.objects.bulk_update(opts, ['percentage'])

        return JsonResponse({
            'voted': True,
            'total_votes': poll.total_votes,
            'options': [
                {'id': o.id, 'label': o.label, 'percentage': o.percentage, 'is_selected': o.is_selected}
                for o in poll.options.all()
            ]
        })
    except PollOption.DoesNotExist:
        return JsonResponse({'error': 'Option not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


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
        post.reactions = list(post.reaction_types.all())
        post.is_liked = False
        post.is_bookmarked = False
        if post.post_type == 'poll' and hasattr(post, 'poll'):
            post.poll_obj = post.poll
            post.poll_options = list(post.poll.options.all())
        else:
            post.poll_obj = None
            post.poll_options = []
        html = _render_post_html(post, request)

        return JsonResponse({'success': True, 'post_html': html, 'post_id': post.id})
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