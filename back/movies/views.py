from django.shortcuts import render, get_object_or_404
from . import crawling
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Genre, Movie, Comment, Score
from .serializers import GenreSerializer, MovieSerializer, CommentSerializer, ScoreSerializer


@api_view(['GET'])
def genres(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreSerializer(genre, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def comments(request, movie_pk):
    comments = Comment.objects.filter(movie=movie_pk).all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def scores(request, movie_pk):
    scores = Score.objects.filter(movie=movie_pk).all()
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)

def movie_crawling(request):
    crawling.themovie_crawling()
    return render(request, 'test.html')