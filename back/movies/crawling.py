from django.shortcuts import get_object_or_404
from .models import Genre, Movie
from bs4 import BeautifulSoup
import requests
import datetime
import os, json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_DIR = os.path.join(BASE_DIR, 'secret_data')

def themovie_crawling():
    """
    input: None
    output: True/False

    the movie db api에서 제공하는 장르, 영화 정보를 가지고 온다.

    권한필요] 관리자
    """
    lan = 'ko-KR'
    size_list = ['w500', 'original']

    with open(os.path.join(SECRET_DIR, 'secret_key.json')) as f:
        data = f.read()
    secret_key = json.loads(data)
    THEMOVIEDB_API = secret_key.get('THEMOVIEDB_API')
    URL = 'https://api.themoviedb.org/3/'

    GENRE_URL = f'{URL}genre/movie/list?api_key={THEMOVIEDB_API}&language={lan}'
    req = requests.get(GENRE_URL)
    if req.status_code == 200:
        genres = req.json().get('genres')
        for genre in genres:
            id = genre.get('id')
            genre_type = genre.get('name')
            Genre.objects.get_or_create(id=id, genre_type=genre_type)

    POSTER_URL = f'https://image.tmdb.org/t/p/'
    MOVIE_URL = f'{URL}discover/movie?api_key={THEMOVIEDB_API}&language={lan}&sort_by=popularity.desc'

    for page in range(1, 6):
        DISCOVER_URL = MOVIE_URL + f'&page={page}'
        req = requests.get(DISCOVER_URL)
        if req.status_code == 200:
            results = req.json().get('results')

            for result in results:
                id = result.get('id')
                title = result.get('title')
                poster = f"{POSTER_URL}{size_list[0]}{result.get('poster_path')}"
                back_image = f"{POSTER_URL}{size_list[1]}{result.get('backdrop_path')}"
                content = result.get('overview')
                open_date = result.get('release_date')[0:4] if result.get('release_date') else ""
                genres = result.get('genre_ids')
                video = ""
                
                VIDEOS_URL = f'{URL}movie/{id}/videos?api_key={THEMOVIEDB_API}&language={lan}'
                req = requests.get(VIDEOS_URL)
                if req.status_code == 200:
                    keys = req.json().get('results')
                    video = keys[0].get('key') if keys else ""
                
                movie = Movie.objects.get_or_create(id=id)
                if movie[1]:
                    movie[0].title = title
                    movie[0].poster = poster
                    movie[0].back_image = back_image
                    movie[0].content = content
                    movie[0].open_date = open_date
                    movie[0].video = video
                    movie[0].save()
                
                    for gen in genres:
                        genre = get_object_or_404(Genre, id=gen)
                        movie[0].genre.add(genre)
