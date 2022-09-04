from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request, *args, **kargs):
    return render(request, 'index.html', {})


def live(request, *args, **kargs):
    return render(request, 'live.html', {})


def fantacy(request, *args, **kargs):
    return render(request, 'fantasy.html', {})


def shop(request, *args, **kargs):
    return render(request, 'shop.html', {})


def about(request, *args, **kargs):
    return render(request, 'about.html', {})


def signin(request, *args, **kargs):
    return render(request, 'signin.html', {})

