from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, SignInForm


def signUp(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account successfully created')
            return redirect('signIn')
        else:
            messages.error(request, 'Incorrect values')
    
    context = {'form': form}

    return render(request, 'user/sign-up.html', context)


def signIn(request):
    form = SignInForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Signed in')
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {'form': form}

    return render(request, 'user/sign-in.html', context)

def logOut(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect('home')
