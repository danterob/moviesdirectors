from django.db import models
from django.conf import settings
from django.urls import reverse


class Directors(models.Model):
    fisrt_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    born_date = models.DateField(blank=True, null=True)
    movie = models.ManyToManyField('Movies', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.fisrt_name}'


class Movies(models.Model):
    title = models.CharField(max_length=60, help_text="Ingrese el titulo")
    description = models.TextField(help_text="Ingrese una breve descripción", blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    genre = models.ManyToManyField('Genre')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies-detail', args=[str(self.id)])


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Ingrese el genero")

    def __str__(self):
        return self.name

class DirectorsMovie(models.Model):
    director = models.ForeignKey('Directors', on_delete=models.CASCADE, blank=True, null=True)
    movie = models.ForeignKey('Movies', on_delete=models.CASCADE, blank=True, null=True)
