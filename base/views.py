from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage


def index(request):
    return render(request, 'base/index.html')


def dashboard(request):
    return render(request, 'base/dashboard.html')


def about(request):
    return render(request, 'base/about.html')


def demo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.FILES.get('file')
        messages.success(
            request, 'Your request has been submitted successfully.')
        return redirect('index')
    return render(request, 'base/demo.html')
