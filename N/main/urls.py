from django.urls import path
from .views import *

urlpatterns = [
    path("", show_start, name="start"),
    path("home", show_home, name="home"),
]
