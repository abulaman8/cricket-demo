from django.shortcuts import render
from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage


def index(request):
    return render(request, 'base/index.html')


def dashboard(request):
    return render(request, 'base/dashboard.html')


def about(request):
    return render(request, 'base/about.html')
