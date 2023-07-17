from django.urls import path 
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/movies

urlpatterns = [
    path("", views.home, name = 'Home'),
    path("home", views.home),
    path("movies", views.movies, name = 'Movies'),
    path("movies/<int:id>", views.moviedetails, name = 'details')
]