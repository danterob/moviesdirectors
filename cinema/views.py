from django.shortcuts import render
from . models import Movies, Genre, Directors


def index(request):
    directors = Directors.objects.all().order_by('fisrt_name')

    return render(request, 'cinema/index.html',
                  {
                      'directors': directors,
                  }
                  )