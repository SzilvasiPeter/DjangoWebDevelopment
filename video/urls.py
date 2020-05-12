from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='video-home'),
    path('about/', views.about, name='video-about'),
]