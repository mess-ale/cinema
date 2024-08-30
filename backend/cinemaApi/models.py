from django.contrib.auth.models import User
from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

class Star(models.Model):
    name = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = models.ImageField(null=True, blank=True, upload_to='movie_images/')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    stars = models.ManyToManyField(Star)
    duration = models.IntegerField()  # Duration in minutes
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    now_playing = models.BooleanField(default=False)
    
class ReleasedMovie(Movie):
    release_date = models.CharField(max_length=100)  # Release date of the movie

    def __str__(self):
        return f"{self.title} (Released on {self.release_date})"

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    format = models.CharField(max_length=20)
    availability = models.CharField(max_length=20)

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchased_at = models.DateTimeField(auto_now_add=True)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)

class MovieRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])