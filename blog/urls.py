from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView, UserPostListView,
                    LikeView, UnlikeView, DislikeView, RemoveDislikeView, 
                    YourEvents, YourPosts, JoinedEvents,LikedEvents,LikedPosts)

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view() , name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'), #pk is the primary key of the post
    path('post/new/', PostCreateView.as_view() , name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='post-delete'),
    path('about/', views.about , name='blog-about'),
    path('post/<int:pk>/like/',LikeView, name='post-like'),
    path('post/<int:pk>/unlike/',UnlikeView, name='post-unlike'),
    path('post/<int:pk>/Dislike/',DislikeView, name='post-dislike'),
    path('post/<int:pk>/RemoveDislike/',RemoveDislikeView, name='post-undislike'),
    path('YourPosts/',YourPosts, name='YourPosts'),
    path('YourEvents/',YourEvents, name='YourEvents'),
    path('JoinedEvents/',JoinedEvents, name='JoinedEvents'),
    path('LikedEvents/',LikedEvents, name='LikedEvents'),
    path('LikedPosts/',LikedPosts, name='LikedPosts'),
]

