from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from .models import Director, Genre, ReleasedMovie, User, Movie
from .serializers import UserSerializer, MovieSerializer, ReleasedMovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from django.db import connection

# Create your views here.

class CreateUsersViews(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class MovieList(APIView):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FilterMovieById(APIView):
    def get(self, request, movie_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM get_movie_by_id(%s)", [movie_id])
            columns = [col[0] for col in cursor.description]
            movie = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(movie)

class MovieNowPlaying(APIView):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.filter(now_playing=True)
        serializer = MovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReleasedMovieList(APIView):
    def get(self, request, *args, **kwargs):
        movies = ReleasedMovie.objects.all()
        serializer = ReleasedMovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FilterMoviesByGenreView(APIView):
    def get(self, request, genre_name):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM filter_movies_by_genre(%s)", [genre_name])
            columns = [col[0] for col in cursor.description]
            movies = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(movies)
    
class FilterMoviesByDirectorView(APIView):
    def get(self, request, director_name):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM filter_movies_by_director(%s)", [director_name])
            columns = [col[0] for col in cursor.description]
            movies = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(movies)

class FilterMoviesByTitleView(APIView):
    def get(self, request, search_term):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM search_movies(%s)", [search_term])
            columns = [col[0] for col in cursor.description]
            movies = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return Response(movies)
    
def get_all_genres_from_movies():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT g.name
            FROM "cinemaApi_movie" m
            JOIN "cinemaApi_genre" g ON m.genre_id = g.id
        """)
        genres = [row[0] for row in cursor.fetchall()]
    return genres

def get_all_directors_from_movies():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT DISTINCT d.name
            FROM "cinemaApi_movie" m
            JOIN "cinemaApi_director" d ON m.director_id = d.id
        """)
        directors = [row[0] for row in cursor.fetchall()]
    return directors


class AllGenresAndDirectorsView(APIView):
    def get(self, request):
        genres = get_all_genres_from_movies()
        directors = get_all_directors_from_movies()
        return Response({
            'genres': genres,
            'directors': directors
        })