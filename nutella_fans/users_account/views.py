from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from users_account.forms import UserCreationForm


def base(request):
    return render(request, 'users_account/base.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('users_account/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'users_account/registration/sign_up.html', {'from': form})


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return render(request, 'users_account/home.html')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'users_account/registration/login.html')


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, 'users_account/home.html')
