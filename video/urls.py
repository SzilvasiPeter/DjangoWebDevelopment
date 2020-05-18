from django.urls import path
from .views import VideoListView, VideoDetailView, RentedVideoListView, VideoCreateView, VideoUpdateView, VideoDeleteView
from . import views

urlpatterns = [
    path('', VideoListView.as_view(), name='video-home'),
    path('video/rented/', RentedVideoListView.as_view(), name='video-rented'),
    path('video/rented/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('video/new/', VideoCreateView.as_view(), name='video-create'),
    path('video/rented/<int:pk>/update', VideoUpdateView.as_view(), name='video-update'),
    path('video/rented/<int:pk>/delete', VideoDeleteView.as_view(), name='video-delete'),
    path('about/', views.about, name='video-about'),
]