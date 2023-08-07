from django.shortcuts import render
from .models import Article

def show_start(request):
    return render(request, 'main/start.html')

def show_home(request):
    article = Article.objects.all()
    data = {
        'article': article
    }
    return render(request, 'main/home.html', data)
