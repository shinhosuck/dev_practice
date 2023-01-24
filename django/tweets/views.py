from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import TweetCreateForm
from tweets.models import Tweet


def home_view(request):
    return render(request, 'tweets/home.html', context=None)


def my_tweet_view(request):
    user = User.objects.get(username = request.user)
    print(user.tweet_set.all())
    return redirect('tweets:home')


def tweet_create_view(request):
    form = TweetCreateForm(request.POST or None)
    print(request.is_ajax())
    redirect_url = request.POST.get('next')
    if form.is_valid():
        new_tweet = form.save()
        obj = Tweet.objects.get(id=new_tweet.id)
        obj.author = request.user
        obj.save()
        print('The form is valid')
        data = {
            'id': obj.id,
            'author': obj.author.username, 
            'title': obj.title,
            'content': obj.content
        }
        return JsonResponse(data)
    else:
        print('The form is not valid')
        data = {
            'error': 'The form is not valid. Tweet title or content is missing.'
        }
        return JsonResponse(data)


def tweets_view(request):
    tweets = Tweet.objects.all()
    tweet_list = [{'id':tweet.id, 'author': tweet.author.username, 'title': tweet.title, 'content': tweet.content } for tweet in tweets]
    data = {'tweets': tweet_list}
    return JsonResponse(data)


def tweet_delete(request, id):
    tweet = Tweet.objects.get(id = int(id))
    print(tweet)
    tweet.delete()
    return JsonResponse(data={'id': int(id)})