from django.shortcuts import render
from .models import Article
from PIL import Image
from typing import List, Any

def optimize_image_size(full_content: dict, max_side: int = 350) -> List[list]:
    image_sizes = []  # [w*h]
    for article in full_content:
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
    return image_sizes

def show_start(request: Any):
    return render(request, 'main/start.html')

def show_home(request: Any):
    articles = Article.objects.all()
    combined_data = zip(articles, optimize_image_size(articles, max_side=350))
    data = {'combined_data': combined_data}
    return render(request, 'main/home.html', data)

def show_lorem(request: Any):
    return render(request, 'surprise/lorem.html')
