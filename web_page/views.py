from django.shortcuts import render

def home(request):
    return render(request, 'web_site/home.html')

