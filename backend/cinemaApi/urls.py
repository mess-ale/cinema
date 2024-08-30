from django.urls import path
from cinemaApi.views import AllGenresAndDirectorsView, CreateUsersViews, MovieList, MovieNowPlaying,FilterMovieById, ReleasedMovieList, FilterMoviesByDirectorView,FilterMoviesByTitleView,FilterMoviesByGenreView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user/register/', CreateUsersViews.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name= 'get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='get_refresh'),
    path('movie/', MovieList.as_view(), name='Movie-list'),
    path('Released-movies/', ReleasedMovieList.as_view(), name='Movie-list'),
    path('nowplaying-movies/', MovieNowPlaying.as_view(), name='Movie-list'),
    path('movies/genre/<str:genre_name>/', FilterMoviesByGenreView.as_view(), name='filter_movies_by_genre'),
    path('movies/director/<str:director_name>/', FilterMoviesByDirectorView.as_view(), name='filter_movies_by_director'),
    path('movies/filter/<str:search_name>/', FilterMoviesByTitleView.as_view(), name='filter_movies_by_title'),
    path('movies/<int:movie_id>/', FilterMovieById.as_view(), name='filter_movies_by_id'),
    path('movies/genres-and-directors/', AllGenresAndDirectorsView.as_view(), name='all_genres_and_directors'),
]
