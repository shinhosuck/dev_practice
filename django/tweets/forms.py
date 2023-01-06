from tweets.models import Tweet
from django import forms


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']