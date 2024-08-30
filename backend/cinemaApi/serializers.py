from rest_framework import serializers
from .models import Director, Star, Genre, Movie, Showtime, Ticket, Bookmark, MovieRating, User, ReleasedMovie

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    director = DirectorSerializer()
    stars = StarSerializer(many=True, read_only=True)
    featured_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_featured_image_url(self, obj):
        request = self.context.get('request')
        if obj.featured_image and request:
            return request.build_absolute_uri(obj.featured_image.url)   
        return None
    
class ReleasedMovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    director = DirectorSerializer()
    stars = StarSerializer(many=True, read_only=True)
    featured_image_url = serializers.SerializerMethodField()

    class Meta:
        model = ReleasedMovie
        fields = '__all__'

    def get_featured_image_url(self, obj):
        request = self.context.get('request')
        if obj.featured_image and request:
            return request.build_absolute_uri(obj.featured_image.url)   
        return None
    
class ShowtimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Showtime
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'

class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = '__all__'