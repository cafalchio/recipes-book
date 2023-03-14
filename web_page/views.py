from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'web_page/index.html')

def login_page(request):        
    return render(request, 'web_page/login.html')

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
