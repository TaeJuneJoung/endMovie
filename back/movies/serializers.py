from rest_framework import serializers
from .models import Genre, Movie, Comment, Score
from accounts.serializers import UserSerializer


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
    users = UserSerializer(source='user', many=False)
    class Meta:
        model = Comment
        fields = ('id', 'movie', 'users', 'content', 'update_at', 'is_update')

class ScoreSerializer(serializers.ModelSerializer):
    users = UserSerializer(source='user', many=False)
    class Meta:
        model = Score
        fields = ('id', 'movie', 'users', 'star', 'create_at')
