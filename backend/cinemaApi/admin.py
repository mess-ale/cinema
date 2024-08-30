from django.contrib import admin
from .models import Bookmark, Director, Genre, Movie, MovieRating, ReleasedMovie, Showtime, Star, Ticket

# Register your models here.
admin.site.register(Bookmark)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieRating)
admin.site.register(Showtime)
admin.site.register(Ticket)
admin.site.register(Star)
admin.site.register(ReleasedMovie)