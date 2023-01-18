from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.http import JsonResponse
from tweets.models import Tweet
from .forms import tweetCreateForm
import random
from django.conf import settings

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request):
    return render(request, template_name='tweets/home.html', context=None)


def tweet_list_view(request):
    all_tweets = Tweet.objects.all()
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
        print(request.is_ajax())
        redirect_url = request.POST.get('next')
        # print(is_safe_url(redirect_url, ALLOWED_HOSTS))
        form = tweetCreateForm(request.POST)
        if form.is_valid():
            new_tweet = form.save()
            data = {'id': new_tweet.id, 'title': new_tweet.title, 'content': new_tweet.content}
            return JsonResponse(data, status=201)
            # if redirect_url and is_safe_url(redirect_url, ALLOWED_HOSTS):
            #     print('valid')
            #     form.save()
            #     return redirect(redirect_url)
            # else:
            #     print('not a safe url')
            #     return redirect(redirect_url)
        else:
            print('not valid')
            return redirect(redirect_url)
    