from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Video(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    duration = models.IntegerField()
    receive_date = models.DateTimeField(auto_now_add=True)

    renter = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'pk': self.pk})
