from django.urls import path
from . import views
from .views import mortalKombatPosts, mortalKombatEvents, SmashEvents, SmashPosts, AllEvents, AllPosts, GGEvents, GGPosts, SFEvents, SFPosts
from blog.models import Post

urlpatterns = [
	path('', views.home, name = 'communities'),
	path('AllPosts/', AllPosts, name = 'All-posts'),
	path('AllEvents/', AllEvents, name = 'All-events'),
	path('GuiltyGearPosts/', GGPosts, name = 'GG-posts'),
	path('GuiltyGearEvents/', GGEvents, name = 'GG-events'),
	path('StreetFighterPosts/', SFPosts, name = 'SF-posts'),
	path('StreetFighterEvents/', SFEvents, name = 'SF-events'),
	path('SmashPosts/', SmashPosts, name = 'Smash-posts'),
	path('SmashEvents/', SmashEvents, name = 'Smash-events'),
	path('MortalKombatPosts/', mortalKombatPosts, name = 'MK-posts'),
	path('MortalKombatEvents/', mortalKombatEvents, name = 'MK-events'),
]