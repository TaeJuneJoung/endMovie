from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    genre_type = models.CharField(max_length=30)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.ManyToManyField(Genre, related_name='movies', blank=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    poster = models.TextField()
    back_image = models.TextField()
    video = models.TextField(blank=True)
    open_date = models.CharField(max_length=4, blank=True)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    goods = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_goods', blank=True)
    report = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_report', blank=True)
    update_at = models.DateTimeField(auto_now=True)
    is_update = models.IntegerField(default=0)

class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    star = models.FloatField(
        validators = (
            MaxValueValidator(5),
            MinValueValidator(0)
        )
    )
    create_at = models.DateTimeField(auto_now_add=True)