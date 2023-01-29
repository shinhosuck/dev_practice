from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


def create_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('tweets:home')
        else:
            print('not valid')
            error = form.errors
            # return redirect('Users:register')
            return render(request, 'Users/form.html', context={'error': error})
    return render(request, 'Users/form.html', context=None)
