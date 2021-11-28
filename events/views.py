from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
 
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
    fields = ['title', 'content', 'event_date', 'community', 'event_type' ]
 
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
 
class EventsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Events
    fields = ['title', 'content', 'event_date', 'community', 'event_type' ]
 
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
    success_url = '/events/'
 
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
