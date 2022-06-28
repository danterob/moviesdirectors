from django.shortcuts import render
from . models import Movies, Genre, Directors


def index(request):
    num_movies = Movies.objects.all().count()
    num_directors = Directors.objects.all().count()

    return render(request, 'cinema/index.html', {})