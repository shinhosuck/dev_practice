from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import TweetCreateForm


def home_view(request):
    return render(request, 'tweets/home.html', context=None)


def tweet_create_view(request):
    form = TweetCreateForm(request.POST or None)
    redirect_url = request.POST.get('next')
    if form.is_valid():
        new_tweet = form.save(commit=None)
        print('The form is valid')
        return redirect(redirect_url)
    else:
        print('The form is not valid')
        return redirect(redirect_url)