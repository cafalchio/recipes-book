from django.shortcuts import render

def home(request):
    return render(request, 'web_page/home.html')

def login(request):
    return render(request, 'web_page/login.html')
