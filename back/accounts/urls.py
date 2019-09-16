from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('users', views.users, name='users'),
    path('user/<int:user_pk>', views.user, name='user'),
]