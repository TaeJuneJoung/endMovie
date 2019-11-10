from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('users', views.users, name='users'),
    path('user/<str:username>', views.user, name='user'),
    path('login', views.login, name='login'),
    path('emailcheck/<str:email>', views.email_check, name='email_check'),
]