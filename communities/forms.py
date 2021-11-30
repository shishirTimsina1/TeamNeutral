from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class RecommenderForm(forms.Form):

	CHOICES_1 = (
		('sm', 'I played a bunch of Nintendo games growing up'),
		('sm2', 'I played or watched a few at a friends house'),
		('sm3', 'I know of them, never played them however'),
		('sm4', 'What is a Mairo'),
		)
	your_name = forms.CharField(label = 'Your name', max_length=50)
	q1 = forms.MultipleChoiceField(label = 'Have you played any Nintendo Games?',
		choices=CHOICES_1, widget=forms.CheckboxSelectMultiple())

	CHOICES_2 = (
		('mk', 'I want to see the pores in the fighters faces'),
		('sf', 'I want realistic proportions and aesthetic'),
		('gg', 'I want over the top designs'),
		)
	q2 = forms.MultipleChoiceField(label = 'How realistic do you want the graphics to be?',
		choices=CHOICES_2, widget=forms.CheckboxSelectMultiple())

	CHOICES_3 = (
		('mk', 'No way, the more gore galore is just more to adore'),
		('mk2', 'No, but there is such a thing as too much'),
		('sm', 'I do not like violence in general'),
		)
	q3 = forms.MultipleChoiceField(label = 'Are you squeamish?',
		choices=CHOICES_3, widget=forms.CheckboxSelectMultiple())

	CHOICES_4 = (
		('sm', 'What?'),
		('sm2', 'Yes, and it scares me'),
		('mk', 'Yea, its at the core of all fighting games'),
		('sf', 'Yup, footsies are the most complex and interesting part'),
		)
	q4 = forms.MultipleChoiceField(label = 'Do you know what footsies are?',
		choices=CHOICES_4, widget=forms.CheckboxSelectMultiple())

	CHOICES_5 = (
		('gg', 'I get dizzy thinking about who to play'),
		('gg2', 'Not usually, but there is a line'),
		('sm', 'More the merrier, gimme all the characters'),
		)
	q5 = forms.MultipleChoiceField(label = 'Do you get ( or think you will get ) overwhelmed when you have too many characters to pick from?',
		choices=CHOICES_5, widget=forms.CheckboxSelectMultiple())

	CHOICES_6 = (
		('gg', 'Huh?'),
		('gg2', 'Love it, it is a must have for a modern fighting game'),
		('gg3', 'I like it, but if the game is fun enough, I do not need it'),
		)
	q6 = forms.MultipleChoiceField(label = 'What is your take on rollback netcode',
		choices=CHOICES_6, widget=forms.CheckboxSelectMultiple())

	CHOICES_7 = (
		('gg', 'Not really my thing'),
		('nt', 'I am neutral on it :)'),
		('gg2', 'If it looks good, it looks good, anime or not'),
		('gg3', 'I enjoy anime in my free time'),
		)
	q7 = forms.MultipleChoiceField(label = 'Opinion on anime aesthetic?',
		choices=CHOICES_7, widget=forms.CheckboxSelectMultiple())

	CHOICES_8 = (
		('gg', 'I want relentless action, constantly on my toes'),
		('mk', 'I want fast action, in small bursts'),
		('sf', 'I like to keep it slow and deliberate'),
		)
	q8 = forms.MultipleChoiceField(label = 'How fast do you want the action to be?',
		choices=CHOICES_8, widget=forms.CheckboxSelectMultiple())

	CHOICES_9 = (
		('mk', 'I mostly play single player'),
		('mk2', 'It is important to have, but multiplayer is the real game'),
		('gg', 'I am here to fight online'),
		)
	q9 = forms.MultipleChoiceField(label = 'How important is single player content to you in a fighting game?',
		choices=CHOICES_9, widget=forms.CheckboxSelectMultiple())

	CHOICES_10 = (
		('sf', 'I have been playing since the arcade days'),
		('sf2', 'Been playing for years'),
		('sm', 'I have tried a few casual games'),
		('sm2', 'What is a fighting game'),
		)
	q10 = forms.MultipleChoiceField(label = 'How much experience do you have with fighting games',
		choices=CHOICES_10, widget=forms.CheckboxSelectMultiple())