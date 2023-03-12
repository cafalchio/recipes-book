from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'web_page/home.html')

@login_required
def logout(request):
    logout(request)
    return redirect('home')
