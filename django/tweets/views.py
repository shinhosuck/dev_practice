from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import TweetCreateForm
from tweets.models import Tweet


def home_view(request):
    return render(request, 'tweets/home.html', context=None)


def tweet_create_view(request):
    form = TweetCreateForm(request.POST or None)
    print(request.is_ajax())
    redirect_url = request.POST.get('next')
    if form.is_valid():
        new_tweet = form.save()
        print('The form is valid')
        data = {
            'id': new_tweet.id,
            'title': new_tweet.title,
            'content': new_tweet.content
        }
        return JsonResponse(data)
        # return redirect(redirect_url)
    else:
        print('The form is not valid')
        data = {
            'error': 'The form is not valid. Tweet title or content is missing.'
        }
        return JsonResponse(data)
        # return redirect(redirect_url)


def tweets_view(request):
    tweets = Tweet.objects.all()
    tweet_list = [{'id':tweet.id, 'title': tweet.title, 'content': tweet.content } for tweet in tweets]
    data = {'tweets': tweet_list}
    return JsonResponse(data)
    # return redirect('tweets:home')