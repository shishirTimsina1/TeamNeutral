from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
 
#data for community drop down
COMMUNITY_CHOICES = (
    ('Mortal Kombat', 'MORTAL KOMBAT'),
    ('Guilty Gear', 'GUILTY GEAR'),
    ('Smash', 'SMASH'),
    ('Street Fighter', 'STREET FIGHTER')
)
 
EVENT_TYPES_CHOICES = (
    ('Friendly', 'FRIENDLY'),
    ('Exhibition', 'EXHIBITION'),
    ('Tournament', 'TOURNAMENT')
)
 
 
#events model
class Events(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    event_date = models.DateTimeField(default= timezone.now)
    community = models.CharField(max_length=20 ,choices=COMMUNITY_CHOICES, default='Mortal Kombat')
    date_posted = models.DateTimeField(default= timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20,choices=EVENT_TYPES_CHOICES, default='Friendly')
    likes = models.ManyToManyField(User, related_name = 'events_likes')
    signed_up = models.ManyToManyField(User, related_name= 'events_signed_up')
    dislikes = models.ManyToManyField(User, related_name = 'events_dislikes')
 
    def total_likes(self):
        return self.likes.count()
 
    def __str__(self):
    	return self.title
 
    def get_absolute_url(self):
        return reverse('events-detail', kwargs = {'pk':self.pk})

