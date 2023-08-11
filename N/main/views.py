from django.shortcuts import render
from .models import Article
from PIL import Image


def show_start(request):
    return render(request, 'main/start.html')


def show_home(request):
    articles = Article.objects.all()

    image_sizes = []  # w*h
    max_side = 350
    for article in articles:
        img = Image.open(article.image)
        width, height = img.size

        if width > max_side or height > max_side:
            aspect_ratio = width / height
            if width > height:
                new_width = max_side
                new_height = int(max_side / aspect_ratio)
            else:
                new_height = max_side
                new_width = int(max_side * aspect_ratio)
        else:
            new_width = width
            new_height = height

        image_sizes.append([new_width, new_height])

    combined_data = zip(articles, image_sizes)
    data = {
        'combined_data': combined_data
    }
    return render(request, 'main/home.html', data)

def show_lorem(request):
    return render(request, 'surprise/lorem.html')
