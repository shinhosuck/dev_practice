from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import TweetCreateForm
from .rest_framework_serializer import TweetSelializer



def home_view(request):
    return render(request, 'tweets/home.html', context=None)


def tweet_create_view(request):
    form = TweetSelializer(data=request.POST)
    print(form.initial_data['content'])
    return JsonResponse({'data':form.initial_data['content']})

def tweet_create_view_pure_jango(request):
    user = request.user
    if user.is_authenticated:
        # if request.method == "POST":
            # redirect_url = request.POST.get('next')
            # print(redirect_url)
        form = TweetCreateForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            data = {
                'title': tweet.title, 
                'content': tweet.content
            }
            return JsonResponse(data)
        print('not a valid form')
        data = {
            'error': 'The form is not valid. Please check the "Title" and "Content" and tweet again.'
        }
        return JsonResponse(data)
        # return redirect(redirect_url)
    else:
        data = {
            'annonymous': 'Please login to tweet'
        }
        return JsonResponse(data)
        # return redirect('tweets:home')


def tweets_view(request):
    return JsonResponse({})


def search_view(request):
    data = request.GET.get('search')
    print(data)
    return render(request, 'tweets/home.html', {'data': data})