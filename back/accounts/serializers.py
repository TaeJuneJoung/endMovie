from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'last_login', 'is_superuser', 'username', 'first_name',
            'last_name', 'email', 'date_joined', 'introduce', 'profile_image',
            'followings', 'pick_movie'
            ]
