from django.urls import path
from .views import (
    CommentListCreateView, CommentDetailView,
    LikePostView, LikeCommentView, FollowUserView,UserSearchView
)

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('comments/<int:comment_id>/like/', LikeCommentView.as_view(), name='like-comment'),
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('search/users/', UserSearchView.as_view(), name='user-search'),
]