from rest_framework import serializers
from .models import User, AuthEmail

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'id', 'last_login', 'username', 'first_name', 'last_name',
            'email', 'date_joined', 'introduce', 'profile_image', 'followings',
            'pick_movie', 'password'
        ]

class UserPostSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'id', 'last_login', 'username', 'first_name', 'last_name',
            'email', 'profile_image', 'password'
        ]

class EmailCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthEmail
        fields = ['email']
