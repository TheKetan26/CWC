"""cwc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page.views import home, live, fantacy, shop, about

from login.views import login

from users.views import new_user, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index', home, name='home'),
    path('fantacy', fantacy, name='fantacy'),
    path('live', live, name='live'),
    path('shop', shop, name='shop'),
    path('about', about, name='about'),

    #Login page
    path('signin', login, name='signin'),

    #New user registration pages
    path('signup', new_user, name='signup'),
    path('register', register, name='about')
]
