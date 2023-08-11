import os
from PIL import Image
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

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     if self.image:
    #         img = Image.open(self.image.path)
    #         max_width = 250
    #         width_percent = (max_width / float(img.size[0]))
    #         height_size = int((float(img.size[1]) * float(width_percent)))
    #         img = img.resize((max_width, height_size), Image.LANCZOS)
    #         img.save(self.image.path)




    
