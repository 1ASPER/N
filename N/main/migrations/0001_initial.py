# Generated by Django 4.2.4 on 2023-08-07 13:48

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('url', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to=main.models.get_image_path)),
                ('time_create', models.DateField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
