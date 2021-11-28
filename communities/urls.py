from django.urls import path
from . import views
from blog.models import Post

urlpatterns = [
	path('', views.home, name = 'communities'),
]