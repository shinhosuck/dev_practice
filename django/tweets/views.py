from django.shortcuts import render, redirect
from django.http import JsonResponse
from tweets.forms import TweetForm

def home_view(request):
    return render(request, 'tweets/home.html', context=None)


def tweet_list_view(request):
    return JsonResponse({'name':'Jane Does'})


def tweet_create_view(request):
    print(request.POST.get('content'))
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form is saved')
            return redirect('tweets:home')
    print('form not saved')
    return redirect('tweets:home')