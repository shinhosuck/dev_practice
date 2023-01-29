from django.urls import path 
from .views import create_user_view


app_name = 'Users'



urlpatterns = [
    path('register', create_user_view, name='register')
]