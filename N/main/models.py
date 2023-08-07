import os
from django.db import models
from datetime import datetime

def get_image_path(instance, filename):
    now = datetime.now()
    year_month_path = now.strftime('%Y/%m')
    return os.path.join(year_month_path, filename)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=100)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to=get_image_path, blank=True)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




    
