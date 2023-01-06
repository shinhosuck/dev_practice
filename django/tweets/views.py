from django.shortcuts import render, redirect
from django.http import JsonResponse
from tweets.forms import TweetForm
from tweets.models import Tweet
def home_view(request):
    return render(request, 'tweets/home.html', context=None)


def tweet_list_view(request):
    all_tweets = Tweet.objects.all().order_by('-id')
    tweets = []
    for tweet in all_tweets:
        tweets.append({'id': tweet.id, 'content': tweet.content})
    data = {
        'tweets': tweets
    }
    return JsonResponse(data)


def tweet_create_view(request):
    print(request.is_ajax())
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form is saved')
            return redirect('tweets:home')
    print('form not saved')
    return redirect('tweets:home')