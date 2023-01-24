from django.urls import path
from .views import (
    home_view,
    my_tweet_view,
    tweet_create_view,
    tweets_view,
    tweet_delete
)


app_name = 'tweets'


urlpatterns = [
    path('', home_view, name='home'),
    path('my/tweets', my_tweet_view, name='my-tweets'),
    path('new/tweet', tweet_create_view, name='new-tweet'),
    path('tweets', tweets_view, name='tweets'),
    path('tweet/delete/<str:id>', tweet_delete, name='tweet-delete')
]