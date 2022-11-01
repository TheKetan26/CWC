from django.shortcuts import render

from users.models import User


def login(request):
    context = request.POST


    return render(request, 'signin.html', {})

