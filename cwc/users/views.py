from django.shortcuts import render

from .models import User


def new_user(request):
    context = request.POST
    return render(request, "signup.html", context)


def register(request):
    context = request.POST

    try:
        if 'gender_female' in context.keys():
            gender = 'female'
        else:
            gender = 'male'

        if len(context['password']) < 8:
            raise Exception("Password Invalid")

        User.objects.create(first_name  = context['first_name'],
                            last_name   = context['last_name'],
                            email       = context['email'],
                            password    = context['password'],
                            contact     = context['contact'],
                            gender      = gender,
                            nation      = 'India')

        return render(request, "signin.html", context)

    except:
        return render(request, "signup.html", context)