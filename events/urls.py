from django.urls import path
from .views import ( EventsListView, EventsDetailView, EventsCreateView, 
                    EventsUpdateView, EventsDeleteView, LikeView, SignupView, 
                    UnlikeView, LeaveEventView, DislikeView, RemoveDislikeView, 
                    AddCommentView, CommentLikeView, CommentRemoveDislikeView, CommentUnlikeView,
                    CommentDislikeView )
from . import views
 
urlpatterns = [
    path('', EventsListView.as_view(), name='events'),
    path('<int:pk>/',EventsDetailView.as_view(), name='events-detail'),
    path('new/', EventsCreateView.as_view(), name = 'events-create'),
    path('<int:pk>/update/',EventsUpdateView.as_view(), name='events-update'),
    path('<int:pk>/delete/',EventsDeleteView.as_view(), name='events-delete'),
    path('<int:pk>/like/',LikeView, name='events-like'),
    path('<int:pk>/SignUp/',SignupView, name='events-signup'),
    path('<int:pk>/unlike/',UnlikeView, name='events-unlike'),
    path('<int:pk>/LeaveEvent/',LeaveEventView, name='events-leave'),
    path('<int:pk>/Dislike/',DislikeView, name='events-dislike'),
    path('<int:pk>/RemoveDislike/',RemoveDislikeView, name='events-undislike'),
    path('<int:pk>/comment/', AddCommentView.as_view() , name='event-add-comment'),
    path('<int:pk>/comment/like/',CommentLikeView, name='event-comment-like'),
    path('<int:pk>/comment/unlike/',CommentUnlikeView, name='event-comment-unlike'),
    path('<int:pk>/comment/Dislike/',CommentDislikeView, name='event-comment-dislike'),
    path('<int:pk>/comment/RemoveDislike/',CommentRemoveDislikeView, name='event-comment-undislike'),
]
