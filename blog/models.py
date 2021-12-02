from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import admin

COMMUNITY_CHOICES = (
    ('Mortal Kombat', 'MORTAL KOMBAT'),
    ('Guilty Gear', 'GUILTY GEAR'),
    ('Smash', 'SMASH'),
    ('Street Fighter', 'STREET FIGHTER'),
	('All', 'ALL')
)


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date_posted = models.DateTimeField(default= timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	community = models.CharField(max_length=20 ,choices=COMMUNITY_CHOICES, default='All')
	dislikes = models.ManyToManyField(User, related_name = 'post_dislikes')
	likes = models.ManyToManyField(User, related_name = 'post_likes')
	image = models.ImageField(null=True, blank=True, upload_to = "post-images/")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk':self.pk})



class templateImages(models.Model):
	name = models.CharField(max_length = 20)
	image = models.ImageField(upload_to="template-images")

class InlineImage(admin.TabularInline):
    model = templateImages
