from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", show_start, name="start"),
    path("home", show_home, name="home"),
    path('l/o/r/e/m/_/i/p/s/u/m', show_lorem, name='lorem')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)