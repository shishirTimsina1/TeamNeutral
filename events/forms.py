from django import forms
from django.forms import widgets
from .models import EventComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = EventComment
        fields = ('name', 'body')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }