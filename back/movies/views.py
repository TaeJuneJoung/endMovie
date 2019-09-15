from django.shortcuts import render
from . import crawling

# Create your views here.
def movie_crawling(request):
    crawling.themovie_crawling()
    return render(request, 'test.html')