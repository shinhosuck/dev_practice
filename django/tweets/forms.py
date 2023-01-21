from .models import Tweet
from django import forms



class TweetCreateForm(forms.ModelForm):
    class Meta:
        model = Tweet 
        fields = ['title', 'content']