from tweets.models import Tweet
from django import forms



class tweetCreateForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['title', 'content']