from django.shortcuts import render, get_object_or_404
from . models import Movies, Genre, Directors


def index(request):
    directors = Directors.objects.all().order_by('fisrt_name')
    directors
    return render(request, 'cinema/index.html', {'directors': directors})


def movie_detail(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    return render(request, 'cinema/movie_detail.html', {'movie': movie})
