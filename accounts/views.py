from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import User
# Create your views here.

def index(request):
    return render(request, 'theme/index.html', {})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.is_bloger = True
            user.save()
            return HttpResponseRedirect(reverse('accounts:user_register'))

        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/user_register.html', {'form': form})  


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active and user.is_bloger:
                login(request, user)
                return HttpResponseRedirect(reverse('blog_app:index'))
            elif user.is_active and user.is_reader:
                login(request, user)

                return HttpResponseRedirect(reverse('accounts:index'))
            else:
                print('user is not active. Please talk to site admin')
                return HttpResponseRedirect(reverse('accounts:index'))
        else:
            print('invalid credentials')
            return HttpResponseRedirect(reverse('accounts:index'))
    else:
        return render(request, 'accounts/login.html', {})



