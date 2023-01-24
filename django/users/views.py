from django.shortcuts import render, redirect



def login_view(request):
    print(request.POST)
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1 is password2:
        print(print('valid password'))
    else:
        print("not valid")
    if request.POST:
        return redirect('tweets:home')
    return render(request, 'users/login.html', context=None)
