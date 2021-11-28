from django.urls import path
from .views import EventsListView, EventsDetailView, EventsCreateView, EventsUpdateView, EventsDeleteView, LikeView, SignupView, UnlikeView, LeaveEventView, DislikeView, RemoveDislikeView
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
]
