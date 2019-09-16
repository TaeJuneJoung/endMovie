from rest_framework import serializers
from .models import Genre, Movie, Comment, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(source='genre', many=True)
    class Meta:
        model = Movie
        fields = ('id', 'genres', 'title', 'content', 'poster', 'back_image', 'video', 'open_date')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'movie', 'user', 'content', 'create_at', 'update_at')

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'movie', 'user', 'content', 'create_at', 'update_at')