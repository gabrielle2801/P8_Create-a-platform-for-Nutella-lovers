from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from users_account.forms import UserCreationForm


def base(request):
    return render(request, 'users_account/base.html')


def home(request):
    return render(request, 'users_account/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'users_account/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'users_account/registration/sign_up.html', {'form': form})


def login_request(request):
    print("test")
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, 'users_account/home.html')
            else:
                messages.error(request, "Invalid username or password.")
                return render(request, 'users_account/registration/login.html')
    else:
        form = AuthenticationForm()
    return render(request, 'users_account/registration/login.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('base')
