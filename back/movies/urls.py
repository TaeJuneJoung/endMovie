from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('genres', views.genres, name='genres'),
    path('genre/<int:genre_pk>', views.genre, name='genre'),
    path('movies', views.movies, name='movies'),
    path('movie/<int:movie_pk>', views.movie, name='movie'),
    path('comments/<int:movie_pk>', views.comments, name='comments'),
    path('comment/<int:comment_pk>', views.comment, name='comment'),
    path('scores/<str:username>', views.scoreUser, name='scoreUser'),
    path('scores/<int:user_pk>/<int:movie_pk>', views.scores, name='scores'),
    path('score/<int:score_pk>', views.score, name='score'),
    path('crawling', views.movie_crawling),
]