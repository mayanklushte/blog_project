from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *


def index(request):
    return render(request, 'blog/index.html', {})


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return HttpResponseRedirect(reverse('blog_app:index'))
        else:
            print(form.errors)
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form':form})
