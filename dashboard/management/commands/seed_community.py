from django.core.management.base import BaseCommand
from dashboard.models import (
    CommunityStory, CommunityChannel, CommunityGame,
    CommunityPost, PostImage, PostTag, PostReaction,
    Poll, PollOption, PollVote,
)


class Command(BaseCommand):
    help = "Seed the database with community demo data."

    def handle(self, *args, **options):
        # Clear existing
        PollOption.objects.all().delete()
        Poll.objects.all().delete()
        PollVote.objects.all().delete()
        PostReaction.objects.all().delete()
        PostTag.objects.all().delete()
        PostImage.objects.all().delete()
        CommunityPost.objects.all().delete()
        CommunityStory.objects.all().delete()
        CommunityChannel.objects.all().delete()
        CommunityGame.objects.all().delete()

        # ── Stories ───────────────────────────────────────────────
        stories = [
            {"username": "shiro",   "avatar_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=100&q=80", "order": 1},
            {"username": "hana",    "avatar_url": "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=100&q=80", "order": 2},
            {"username": "mika",    "avatar_url": "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=100&q=80", "order": 3},
            {"username": "ren",     "avatar_url": "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=100&q=80", "order": 4},
            {"username": "yuki",    "avatar_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=100&q=80", "is_seen": True, "order": 5},
            {"username": "kai",     "avatar_url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=100&q=80", "order": 6},
            {"username": "aoi",     "avatar_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=100&q=80", "order": 7},
            {"username": "takumi",  "avatar_url": "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=100&q=80", "is_seen": True, "order": 8},
        ]
        for s in stories:
            CommunityStory.objects.create(**s)

        # ── Channels ──────────────────────────────────────────────
        channels = [
            {"name": "general",       "slug": "general",       "icon": "hash",          "post_count": 24},
            {"name": "screenshots",   "slug": "screenshots",   "icon": "image",         "post_count": 128},
            {"name": "fan-art",       "slug": "fan-art",       "icon": "palette",       "post_count": 87},
            {"name": "guides",        "slug": "guides",        "icon": "book-open",     "post_count": 42},
            {"name": "lfg",           "slug": "lfg",           "icon": "gamepad-2",     "post_count": 18},
            {"name": "merch-trading", "slug": "merch-trading", "icon": "shopping-bag",  "post_count": 56},
            {"name": "cosplay",       "slug": "cosplay",       "icon": "sparkles",      "post_count": 34},
        ]
        ch_objs = {}
        for c in channels:
            obj = CommunityChannel.objects.create(**c)
            ch_objs[c["slug"]] = obj

        # ── Games You Follow ──────────────────────────────────────
        games = [
            {"name": "Project Sekai",        "image_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80", "is_active": True,  "order": 1},
            {"name": "Genshin Impact",       "image_url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=80&q=80", "is_active": False, "order": 2},
            {"name": "Honkai: Star Rail",    "image_url": "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=80&q=80", "is_active": True,  "order": 3},
            {"name": "Elden Ring",           "image_url": "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80", "is_active": False, "order": 4},
            {"name": "Persona 3 Reload",     "image_url": "https://images.unsplash.com/photo-1592853625601-bb9d23da12fc?auto=format&fit=crop&w=80&q=80", "is_active": False, "order": 5},
        ]
        for g in games:
            CommunityGame.objects.create(**g)

        # ── Posts ─────────────────────────────────────────────────

        # -- POST 1: Pinned Announcement --
        p1 = CommunityPost.objects.create(
            post_type="announcement",
            title="🎮 Summer Sale 2026 is HERE — Up to 80% off!",
            content="The biggest sale of the year just dropped. Get exclusive discounts on games, figures, and merch from your favorite anime series. Sale ends August 31st.",
            author_name="Kaimono Official",
            author_avatar="https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=100&q=80",
            author_badge="verified",
            channel=ch_objs["general"],
            is_pinned=True,
            time_ago="2 hours ago",
            reaction_count=2481,
            comment_count=342,
            share_count=1204,
        )
        PostImage.objects.create(post=p1, url="https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=800&q=80", order=0)
        PostReaction.objects.create(post=p1, reaction_type="heart")
        PostReaction.objects.create(post=p1, reaction_type="thumbs-up")

        # -- POST 2: Image Post --
        p2 = CommunityPost.objects.create(
            post_type="image",
            content='Finally got the perfect shot of the new event stage! The lighting in this update is absolutely stunning 📸 #ProjectSekai',
            author_name="shiro_kun",
            author_avatar="https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=100&q=80",
            channel=ch_objs["screenshots"],
            time_ago="3 hours ago",
            reaction_count=341,
            comment_count=42,
            share_count=88,
        )
        PostImage.objects.create(post=p2, url="https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=400&q=80", order=0)
        PostImage.objects.create(post=p2, url="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=400&q=80", order=1)
        PostImage.objects.create(post=p2, url="https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=400&q=80", order=2)
        PostImage.objects.create(post=p2, url="https://images.unsplash.com/photo-1592853625601-bb9d23da12fc?auto=format&fit=crop&w=400&q=80", order=3)
        PostReaction.objects.create(post=p2, reaction_type="heart")
        PostReaction.objects.create(post=p2, reaction_type="camera")
        PostTag.objects.create(post=p2, name="ProjectSekai")

        # -- POST 3: Poll --
        p3 = CommunityPost.objects.create(
            post_type="poll",
            content="",
            author_name="hana_illustrator",
            author_avatar="https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=100&q=80",
            channel=ch_objs["general"],
            time_ago="5 hours ago",
            reaction_count=0,
            comment_count=128,
            share_count=42,
        )
        poll = Poll.objects.create(
            post=p3,
            question="Which upcoming game are you most hyped for?",
            total_votes=1284,
            time_left="3 days left",
        )
        opt_silksong = PollOption.objects.create(poll=poll, label="Silksong", percentage=48, order=0)
        opt_gta = PollOption.objects.create(poll=poll, label="GTA VI", percentage=29, order=1)
        opt_metroid = PollOption.objects.create(poll=poll, label="Metroid Prime 4", percentage=15, order=2)
        opt_fable = PollOption.objects.create(poll=poll, label="Fable", percentage=8, order=3)

        # Seed per-user votes so percentages/count look realistic (48/29/15/8 ≈ 1284).
        dist = [
            (opt_silksong, 48),
            (opt_gta, 29),
            (opt_metroid, 15),
            (opt_fable, 8),
        ]
        votes = []
        n = 1
        for opt, pct in dist:
            for _ in range(round(1284 * pct / 100)):
                votes.append(PollVote(poll=poll, option=opt, user_name=f"voter_{n}"))
                n += 1
        PollVote.objects.bulk_create(votes)

        # -- POST 4: Discussion --
        p4 = CommunityPost.objects.create(
            post_type="discussion",
            title="LF: Authentic Nendoroid Ichika (1st press) — WTB or Trade",
            content="Hey everyone! I've been hunting for the first press edition of the Ichika Nendoroid for months now. I'm willing to pay a fair price or trade for my duplicate Miku V4X figure.",
            author_name="mikaelle",
            author_avatar="https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=100&q=80",
            channel=ch_objs["merch-trading"],
            time_ago="8 hours ago",
            reaction_count=87,
            comment_count=32,
            share_count=12,
        )
        PostTag.objects.create(post=p4, name="LF", is_highlighted=True)
        PostTag.objects.create(post=p4, name="nendoroid")
        PostTag.objects.create(post=p4, name="projectsekai")
        PostTag.objects.create(post=p4, name="trading")
        PostReaction.objects.create(post=p4, reaction_type="thumbs-up")

        # -- POST 5: Guide --
        p5 = CommunityPost.objects.create(
            post_type="guide",
            content="Just published my comprehensive guide on maximizing crystal farming in the new Honkai update.",
            author_name="ren_dev",
            author_avatar="https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=100&q=80",
            author_badge="verified",
            channel=ch_objs["guides"],
            time_ago="Yesterday",
            reaction_count=2341,
            comment_count=198,
            share_count=487,
            view_count=18000,
            bookmark_count=842,
        )
        # Guide link card image
        PostImage.objects.create(
            post=p5,
            url="https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=800&q=80",
            caption="Ultimate Crystal Farming Guide v2.4 — 10x Efficiency",
            order=0,
        )
        PostReaction.objects.create(post=p5, reaction_type="heart")
        PostReaction.objects.create(post=p5, reaction_type="star")

        # -- POST 6: Discussion (extra for pagination) --
        p6 = CommunityPost.objects.create(
            post_type="discussion",
            title="Best anime figure stores in Tokyo? Visiting next month!",
            content="I'm planning a trip to Tokyo and want to hit up the best figure stores. Akihabara is a given, but any hidden gems? Looking for both new releases and vintage finds. Budget is around ¥50,000.",
            author_name="yuki_traveler",
            author_avatar="https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=100&q=80",
            channel=ch_objs["merch-trading"],
            time_ago="12 hours ago",
            reaction_count=156,
            comment_count=67,
            share_count=23,
        )
        PostTag.objects.create(post=p6, name="tokyo")
        PostTag.objects.create(post=p6, name="figures")
        PostTag.objects.create(post=p6, name="travel")
        PostReaction.objects.create(post=p6, reaction_type="heart")

        # -- POST 7: Image (extra) --
        p7 = CommunityPost.objects.create(
            post_type="image",
            content="My Genshin Impact shrine setup is finally complete! 🏮 The Raiden Shogun statue was the last piece. #GenshinImpact #Shrine",
            author_name="kai_builder",
            author_avatar="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=100&q=80",
            channel=ch_objs["fan-art"],
            time_ago="1 day ago",
            reaction_count=523,
            comment_count=89,
            share_count=134,
        )
        PostImage.objects.create(post=p7, url="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=400&q=80", order=0)
        PostImage.objects.create(post=p7, url="https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=400&q=80", order=1)
        PostTag.objects.create(post=p7, name="GenshinImpact")
        PostTag.objects.create(post=p7, name="Shrine")
        PostReaction.objects.create(post=p7, reaction_type="heart")
        PostReaction.objects.create(post=p7, reaction_type="camera")

        # -- POST 8: Discussion (extra) --
        p8 = CommunityPost.objects.create(
            post_type="discussion",
            title="Co-op partner needed for Honkai Star Rail endgame content",
            content="Looking for an active player to team up for Memory of Chaos and Simulated Universe. I'm TL65 with most meta characters built. DM me your UID!",
            author_name="aoi_gamer",
            author_avatar="https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=100&q=80",
            channel=ch_objs["lfg"],
            time_ago="2 days ago",
            reaction_count=34,
            comment_count=28,
            share_count=5,
        )
        PostTag.objects.create(post=p8, name="LFG")
        PostTag.objects.create(post=p8, name="HonkaiStarRail")
        PostReaction.objects.create(post=p8, reaction_type="thumbs-up")

        total_posts = CommunityPost.objects.count()
        total_stories = CommunityStory.objects.count()
        total_channels = CommunityChannel.objects.count()
        total_games = CommunityGame.objects.count()
        total_polls = Poll.objects.count()

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded community: {total_posts} posts, {total_stories} stories, "
                f"{total_channels} channels, {total_games} games, {total_polls} polls."
            )
        )
