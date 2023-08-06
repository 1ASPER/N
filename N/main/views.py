from django.shortcuts import render

def show_start(request):
    return render(request, 'main/start.html')

def show_home(request):
    return render(request, 'main/home.html')
