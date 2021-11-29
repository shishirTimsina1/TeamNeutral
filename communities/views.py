from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from blog.models import Post
from django.db.models import Q
from events.models import Events

# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'communities/community-home.html', context)

def AllPosts(request):
	context = {
		'posts': Post.objects.order_by('-date_posted').all()
	}
	return render(request, 'communities/All-posts.html', context)

def AllEvents(request):
	context = {
		'events': Events.objects.order_by('-date_posted').all()
	}
	return render(request, 'communities/All-events.html', context)

def mortalKombatPosts(request):
	context = {
		'posts': Post.objects.filter(Q(community = 'Mortal Kombat') | Q(community='All')).order_by('-date_posted').all()
	}
	return render(request, 'communities/mortalKombat-posts.html', context)

def mortalKombatEvents(request):
	context = {
		'events': Events.objects.filter(Q(community = 'Mortal Kombat') | Q(community='All')).order_by('-date_posted').all()
	}
	return render(request, 'communities/mortalKombat-events.html', context)

def SmashPosts(request):
	context = {
		'posts': Post.objects.filter(Q(community = 'Smash') | Q(community='All')).order_by('-date_posted').all()
	}
	return render(request, 'communities/Smash-posts.html', context)

def SmashEvents(request):
	context = {
		'events': Events.objects.filter(Q(community = 'Smash') | Q(community='All')).order_by('-date_posted').all()
	}
	return render(request, 'communities/Smash-events.html', context)

def GGPosts(request):
	context = {
		'posts': Post.objects.filter(Q(community = 'Guilty Gear') | Q(community='All')).order_by('-date_posted').all()
	}
	return render(request, 'communities/GG-posts.html', context)

def GGEvents(request):
	context = {
		'events': Events.objects.filter(Q(community = 'Guilty Gear') | Q(community='All')).order_by('-date_posted').all()
	}
	return render(request, 'communities/GG-events.html', context)

def SFPosts(request):
	context = {
		'posts': Post.objects.filter(Q(community = 'Street Fighter') | Q(community='All')).order_by('-date_posted').all()
	}
	return render(request, 'communities/SF-posts.html', context)

def SFEvents(request):
	context = {
		'events': Events.objects.filter(Q(community = 'Street Fighter') | Q(community='All')).order_by('-date_posted').all()
	}
	return render(request, 'communities/SF-events.html', context)