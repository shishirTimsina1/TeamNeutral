from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
from events.models import Events
from LearnDjango import settings
from .forms import CommentForm

# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.all()
	}

	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

def Tutorial(request):
	return render(request, 'blog/tutorial.html', {'title': 'How To Use Neutral'})
	
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields =  ['title', 'content', 'community', 'image']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields =  ['title', 'content', 'community', 'image']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
	
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def LikeView(request, pk):
    post = get_object_or_404(Post, id = pk)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def UnlikeView(request, pk):
    post = get_object_or_404(Post, id = pk)
    post.likes.remove(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def DislikeView(request, pk):
    post = get_object_or_404(Post, id = pk)
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def RemoveDislikeView(request, pk):
    post = get_object_or_404(Post, id = pk)
    post.dislikes.remove(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def YourPosts(request):
	context = {
		'posts': Post.objects.order_by('-date_posted').all()
	}
	return render(request, 'blog/YourPosts.html', context)

def LikedPosts(request):
	context = {
		'posts': Post.objects.order_by('-date_posted').all()
	}
	return render(request, 'blog/LikedPosts.html', context)

def LikedEvents(request):
	context = {
		'events': Events.objects.order_by('-date_posted').all()
	}
	return render(request, 'blog/LikedEvents.html', context)

def JoinedEvents(request):
	context = {
		'events': Events.objects.order_by('-date_posted').all()
	}
	return render(request, 'blog/JoinedEvents.html', context)

def YourEvents(request):
	context = {
		'events': Events.objects.order_by('-date_posted').all()
	}
	return render(request, 'blog/YourEvents.html', context)

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'blog/add_comment.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

def CommentLikeView(request, pk):
	comment = get_object_or_404(Comment, id = pk)
	comment.likes.add(request.user)
	post = comment.post
	returnPK = post.id
	return HttpResponseRedirect(reverse('post-detail', args=[str(returnPK)]))

def CommentUnlikeView(request, pk):
	comment = get_object_or_404(Comment, id = pk)
	comment.likes.remove(request.user)
	post = comment.post
	returnPK = post.id
	return HttpResponseRedirect(reverse('post-detail', args=[str(returnPK)]))

def CommentDislikeView(request, pk):
	comment = get_object_or_404(Comment, id = pk)
	comment.dislikes.add(request.user)
	post = comment.post
	returnPK = post.id
	return HttpResponseRedirect(reverse('post-detail', args=[str(returnPK)]))

def CommentRemoveDislikeView(request, pk):
	comment = get_object_or_404(Comment, id = pk)
	comment.dislikes.remove(request.user)
	post = comment.post
	returnPK = post.id
	return HttpResponseRedirect(reverse('post-detail', args=[str(returnPK)]))