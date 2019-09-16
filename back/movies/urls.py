from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('genres', views.genres, name='genres'),
    path('genre/<int:genre_pk>', views.genre, name='genre'),
    path('movies', views.movies, name='movies'),
    path('movie/<int:movie_pk>', views.movie, name='movie'),
    path('comment/<int:movie_pk>', views.comments, name='comments'),
    path('score/<int:movie_pk>', views.scores, name='scores'),
]