from django.urls import path
from .views import (
    home_view,
    tweet_create_view,
    search_view,
    tweets_view
)


app_name = 'tweets'



urlpatterns = [
    path('', home_view, name='home'),
    path('new/tweet', tweet_create_view, name='new-tweet'),
    path('tweets', tweets_view, name='tweets'),
    path('search', search_view, name='search')

]