from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.movie_detail, name="movie_detail"),
]
