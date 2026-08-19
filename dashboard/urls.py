from django.urls import path
from django.contrib.auth.decorators import login_required

from accounts import views as auth
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', auth.login_view, name='login'),
    path('register/', auth.register_view, name='register'),
    path('logout/', auth.logout_view, name='logout'),
    path('accsetup/', auth.accsetup_view, name='accsetup'),
    path('profile/', login_required(auth.profile_view), name='profile'),
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:product_id>/', views.game_detail, name='game_detail'),
    path('community/', views.community, name='community'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('library/', views.library, name='library'),
    path('settings/', login_required(auth.settings_view), name='settings'),
    path('settings/delete-account/', login_required(auth.delete_account_view), name='delete_account'),
    path('settings/admin/', views.admin_panel, name='admin_panel'),
    path('settings/developer/', views.developer_panel, name='developer_panel'),
    path('settings/developer/submit/', views.developer_panel_submit, name='developer_panel_submit'),
    # Community AJAX endpoints
    path('api/community/vote/', views.community_vote_poll, name='community_vote_poll'),
    path('api/community/post/', views.community_create_post, name='community_create_post'),
    path('api/community/post/edit/', views.community_edit_post, name='community_edit_post'),
    path('api/community/post/delete/', views.community_delete_post, name='community_delete_post'),
    path('api/community/comment/', views.community_add_comment, name='community_add_comment'),
    path('api/community/comments/', views.community_get_comments, name='community_get_comments'),
    path('api/community/share/', views.community_share_post, name='community_share_post'),
    path('api/community/games/follow/', views.community_toggle_follow_game, name='community_toggle_follow_game'),
    path('api/shop/checkout/', views.checkout_complete, name='checkout_complete'),
    path('api/shop/check-ownership/', views.api_check_ownership, name='api_check_ownership'),
    path('api/wishlist/toggle/', views.api_wishlist_toggle, name='api_wishlist_toggle'),
    path('api/wishlist/list/', views.api_wishlist_list, name='api_wishlist_list'),
    path('api/reviews/', views.api_game_reviews, name='api_game_reviews'),
    path('api/reviews/submit/', views.api_game_review_submit, name='api_game_review_submit'),
]