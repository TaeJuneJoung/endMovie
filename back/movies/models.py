from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    genre_type = models.CharField(max_length=30)

class Movie(models.Model):
    genre = models.ManyToManyField(Genre, related_name='movies', blank=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    poster = models.TextField()
    back_image = models.TextField()
    open_date = models.CharField(max_length=4, blank=True)
