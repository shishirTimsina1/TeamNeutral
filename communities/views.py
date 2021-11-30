from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from blog.models import Post
from django.db.models import Q
from events.models import Events
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, RecommenderForm
from django.contrib import messages
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

def recommender(request):
	# scores index in order, 0 = Smash, 1 = MK, 2 = GG, 3 = SF
	scores = [0,0,0,0]


	if request.method == 'POST':
		form = RecommenderForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('your_name')
			#print(username)
			answer1 = form.cleaned_data.get('q1')
			#messages.success(request, f'asnwer 1 = {answer1}')
			if(answer1[0] == 'sm'):
				scores[0] += 10
			elif(answer1[0] == 'sm2'):
				scores[0] += 5
			elif(answer1[0] == 'sm3'):
				scores[0] += 3
			elif(answer1[0] == 'sm4'):
				scores[0] -= 2

			answer2 = form.cleaned_data.get('q2')
			if(answer2[0] == 'mk'):
				scores[0] -= 3
				scores[1] += 5
				scores[2] += 1
				scores[3] += 2
			elif(answer2[0] == 'sf'):
				scores[1] += 3
				scores[2] += 2
				scores[3] += 5
			elif(answer2[0] == 'gg'):
				scores[0] += 2
				scores[1] += 1
				scores[2] += 5
				scores[3] += 3

			answer3 = form.cleaned_data.get('q3')
			if(answer3[0] == 'mk'):
				scores[0] -= 4
				scores[1] += 8
			elif(answer3[0] == 'mk2'):
				scores[0] -= 2
				scores[1] += 4
				scores[2] += 1
				scores[3] += 2
			elif(answer3[0] == 'sm'):
				scores[0] += 4

			answer4 = form.cleaned_data.get('q4')
			if(answer4[0] == 'sm'):
				scores[0] += 3
				scores[1] += 1
				scores[2] += 2
				scores[3] -= 1
			elif(answer4[0] == 'sm2'):
				scores[0] += 4
				scores[1] += 1
				scores[2] += 2
				scores[3] -= 5
			elif(answer4[0] == 'mk'):
				scores[1] += 2
				scores[2] += 1
				scores[3] += 4
			elif(answer4[0] == 'sf'):
				scores[0] -= 3
				scores[1] += 3
				scores[2] += 2
				scores[3] += 5

			answer5 = form.cleaned_data.get('q5')
			if(answer5[0] == 'gg'):
				scores[0] -= 5
				scores[1] -= 2
				scores[2] += 3
				scores[3] -= 1
			elif(answer5[0] == 'gg2'):
				scores[0] -= 1
				scores[1] += 1
				scores[2] += 2
				scores[3] += 2
			elif(answer5[0] == 'sm'):
				scores[0] += 5
				scores[1] += 3
				scores[3] += 3
			winner = max(scores)
			index = scores.index(winner)
			com = ''
			if(index == 0):
				com = 'Smash Bros'
			elif(index == 1):
				com = 'Mortal Kombat'
			elif(index == 2):
				com = 'Guilty Gear'
			elif(index == 3):
				com = 'Street Fighter'
			messages.success(request, f'Form submitted, {username} You should join {com} with scores{scores}')
			return redirect('communities')
	else:
		form = RecommenderForm()
	return render(request, 'communities/recommender.html', {'form': form})