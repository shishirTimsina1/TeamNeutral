from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events, EventComment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .forms import CommentForm
 
# Create your views here.
 
"""
Dummy data used for testing before database was made
Cur_events = [
    {
        'creator': 'Chris',
        'title': 'First Event',
        'community': 'Mortal Kombat',
        'content': 'First Event Content',
        'date_posted': 'November 27, 2021',
        'event_date': 'November 30, 2021',
        'event_type': 'Friendly',
    },
    {
        'creator': 'Christopher',
        'title': 'Second Event',
        'community': 'Guilty Gear',
        'content': 'Second Event Content',
        'date_posted': 'November 27, 2021',
        'event_date': 'December 25, 2021',
        'event_type': 'Friendly',
    }
]
"""
 
def events(request):
    context = {
        'events': Events.objects.all(),
    }
    return render(request, 'events/events.html', context)
 
class EventsListView(ListView):
    model = Events
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['-date_posted']
 
class EventsDetailView(DetailView):
    model = Events
 
 
class EventsCreateView(LoginRequiredMixin, CreateView):
    model = Events
    fields = ['title', 'content', 'event_date', 'community', 'event_type', 'image' ]
 
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
 
class EventsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Events
    fields = ['title', 'content', 'image' ]
 
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
 
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.creator:
            return True
        return False
 
class EventsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Events
    success_url = '/'
 
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.creator:
            return True
        return False
 
#save the like to the database
def LikeView(request, pk):
    event = get_object_or_404(Events, id = pk)
    event.likes.add(request.user)
    return HttpResponseRedirect(reverse('events-detail', args=[str(pk)]))
 
def SignupView(request,pk):
    print('in signup')
    event = get_object_or_404(Events, id = pk)
    print('found event')
    event.signed_up.add(request.user)
    return HttpResponseRedirect(reverse('events-detail', args=[str(pk)]))
 
def UnlikeView(request, pk):
    event = get_object_or_404(Events, id = pk)
    event.likes.remove(request.user)
    return HttpResponseRedirect(reverse('events-detail', args=[str(pk)]))
 
def LeaveEventView(request,pk):
    event = get_object_or_404(Events, id = pk)
    event.signed_up.remove(request.user)
    return HttpResponseRedirect(reverse('events-detail', args=[str(pk)]))
 
def DislikeView(request, pk):
    event = get_object_or_404(Events, id = pk)
    event.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('events-detail', args=[str(pk)]))
 
def RemoveDislikeView(request, pk):
    event = get_object_or_404(Events, id = pk)
    event.dislikes.remove(request.user)
    return HttpResponseRedirect(reverse('events-detail', args=[str(pk)]))

class AddCommentView(CreateView):
	model = EventComment
	form_class = CommentForm
	template_name = 'events/add_comment.html'
	success_url = '/'

	def form_valid(self, form, request):
		form.instance.event_id = self.kwargs['pk']
		return super().form_valid(form)

def CommentLikeView(request, pk):
	comment = get_object_or_404(EventComment, id = pk)
	comment.likes.add(request.user)
	event = comment.event
	returnPK = event.id
	return HttpResponseRedirect(reverse('events-detail', args=[str(returnPK)]))

def CommentUnlikeView(request, pk):
	comment = get_object_or_404(EventComment, id = pk)
	comment.likes.remove(request.user)
	event = comment.event
	returnPK = event.id
	return HttpResponseRedirect(reverse('events-detail', args=[str(returnPK)]))

def CommentDislikeView(request, pk):
	comment = get_object_or_404(EventComment, id = pk)
	comment.dislikes.add(request.user)
	event = comment.event
	returnPK = event.id
	return HttpResponseRedirect(reverse('events-detail', args=[str(returnPK)]))

def CommentRemoveDislikeView(request, pk):
	comment = get_object_or_404(EventComment, id = pk)
	comment.dislikes.remove(request.user)
	event = comment.event
	returnPK = event.id
	return HttpResponseRedirect(reverse('events-detail', args=[str(returnPK)]))