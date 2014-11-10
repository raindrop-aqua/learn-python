# coding: utf-8

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

from forms import LoginForm


def login_view(request):
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = 'You logged in with success.'
                else:
                    message = 'Your user is inactive.'
            else:
                message = 'Invalid username and/or password.'
    else:
        form = LoginForm()
    return render_to_response('jumpingintojango/login.html',
                              {'message': message, 'form': form},
                              context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return redirect('home')


def home(request):
    return render_to_response('jumpingintojango/home.html',
                              context_instance=RequestContext(request))

