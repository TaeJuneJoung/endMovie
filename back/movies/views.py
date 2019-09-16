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

@api_view(['GET', 'PUT', 'DELETE'])
def comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, many=False, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        comment.delete()
        return Response({'message':'삭제되었습니다.'})

@api_view(['GET'])
def scores(request, movie_pk):
    scores = Score.objects.filter(movie=movie_pk).all()
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def score(request, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    if request.method == 'PUT':
        serializer = ScoreSerializer(score, many=False, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        score.delete()
        return Response({'message':'삭제되었습니다.'})

def movie_crawling(request):
    crawling.themovie_crawling()
    return render(request, 'test.html')
