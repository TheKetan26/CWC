from django.shortcuts import render

from users.models import User


def login(request):
    context = request.POST

    obj = User.objects.get(email='u@gmqil.com')
    print(obj)


    return render(request, 'signin.html', {})

