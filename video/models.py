from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    duration = models.IntegerField()
    receive_date = models.DateTimeField(auto_now_add=True)
    isRented = models.BooleanField(default=False)

    # TODO: when deleting user set the video isRented field to False
    renter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title







    # 'title': 'Devs',
    # 'genre': 'Sci-Fi',
    # 'duration': 50,
    # 'release_dates': '2020.01.01'