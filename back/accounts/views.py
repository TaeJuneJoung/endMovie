from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, AuthEmail
from .serializers import UserSerializer, UserPostSerializer, EmailCheckSerializer
from .authentication import auth_email_check

@api_view(['GET', 'PUT'])
def email_check(request, email):
    if request.method == 'GET':
        try:
            auth_nums = auth_email_check(email)
            auth_email = AuthEmail.objects.get_or_create(email=email)
            auth_email[0].authentication=auth_nums
            auth_email[0].save()
        except:
            auth_nums = False
        finally:
            return Response({'result': auth_nums})
    else:
        pass

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user, many=False, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            user = get_user_model().objects.create_user(**serializer.data)
            return Response({'message':'생성되었습니다.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, many=False, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        user.delete()
        return Response({'message':'삭제되었습니다.'})