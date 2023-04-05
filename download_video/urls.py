from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("", views.download_video, name="index"),
    path("info_video/", csrf_exempt(views.info_video), name="info_video")
]
