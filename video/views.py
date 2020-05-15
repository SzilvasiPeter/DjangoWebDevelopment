from django.shortcuts import render
from django.http import HttpResponse

videos = [
    {
        'title': 'Devs',
        'genre': 'Sci-Fi',
        'duration': 50,
        'release_dates': '2020.01.01'
    },
    {
        'title': 'WestWorld',
        'genre': 'Sci-Fi',
        'duration': 45,
        'release_dates': '2018.02.01'
    }
]

rented_videos = [
    {
        'title': 'Breaking Bad',
        'genre': 'Action',
        'duration': 35,
        'release_dates': '2015.06.12'
    },
]


def home(request):
    context = {
        'videos': videos,
        'rented_videos': rented_videos
    }
    return render(request, 'video/home.html', context=context)


def about(request):
    return render(request, 'video/about.html')
