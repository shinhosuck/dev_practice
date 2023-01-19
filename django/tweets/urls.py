from django.urls import path
from .views import (
    home_view,
    tweet_create_view
)


app_name = 'tweets'


urlpatterns = [
    path('', home_view, name='home'),
    path('new/tweet', tweet_create_view, name='new-tweet')
]