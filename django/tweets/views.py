from django.shortcuts import render, redirect
from django.http import JsonResponse
from tweets.models import Tweet
from .forms import tweetCreateForm
import random

def home_view(request):
    return render(request, template_name='tweets/home.html', context=None)


def tweet_list_view(request):
    all_tweets = Tweet.objects.all().order_by('-id')
    tweet_list = []
    for tweet in all_tweets:
        likes = random.randint(0, 100)
        follow = random.randint(0, 100)
        tweet_list.append({'id': tweet.id, 'title': tweet.title, 'content': tweet.content, 'likes': likes, 'follow': follow})
    data = {
        'tweets': tweet_list,
    }
    return JsonResponse(data)


def tweet_create_view(request):
    if request.method == 'POST':
        form = tweetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print('valid')
            return redirect('tweets:home')
        print('not valid')
        return redirect('tweets:home')
    