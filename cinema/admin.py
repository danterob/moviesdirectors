from django.contrib import admin
from .models import Movies, Genre, Directors

admin.site.register(Movies)
admin.site.register(Genre)
admin.site.register(Directors)
