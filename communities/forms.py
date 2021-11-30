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
	q4 = forms.MultipleChoiceField(label = 'Are you squeamish?',
		choices=CHOICES_4, widget=forms.CheckboxSelectMultiple())

	CHOICES_5 = (
		('gg', 'I get dizzy thinking about who to play'),
		('gg2', 'Not usually, but there is a line'),
		('sm', 'More the merrier, gimme all the characters'),
		)
	q5 = forms.MultipleChoiceField(label = 'Do you get ( or think you will get ) overwhelmed when you have too many characters to pick from?',
		choices=CHOICES_5, widget=forms.CheckboxSelectMultiple())

	CHOICES_6 = (
		(),
		(),
		(),
		(),
		)
	q6 = forms.MultipleChoiceField(label = 'Do you get ( or think you will get ) overwhelmed when you have too many characters to pick from?',
		choices=CHOICES_6, widget=forms.CheckboxSelectMultiple())
	CHOICES_2 = (
		(),
		(),
		(),
		(),
		)
	CHOICES_2 = (
		(),
		(),
		(),
		(),
		)
	CHOICES_2 = (
		(),
		(),
		(),
		(),
		)
	CHOICES_2 = (
		(),
		(),
		(),
		(),
		)