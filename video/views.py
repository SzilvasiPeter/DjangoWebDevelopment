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


def home(request):
    context = {
        'videos': videos
    }
    return render(request, 'video/home.html', context)


def about(request):
    return render(request, 'video/about.html')
