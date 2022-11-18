from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Actor, Genre, Rating

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'vote_average', 'vote_count')

class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres', 'overview')


class TopMovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'



class MovieSearchSerializer(serializers.ModelSerializer):

    similarity = serializers.FloatField(default=0)

    class Meta:
        model = Movie
        fields = ('pk', 'overview', 'title', 'poster_path', 'similarity',)

# 유저 정보
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'nickname')
        
# 평점
class RatingSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields =('pk', 'username',)

    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields= '__all__'
        read_only_fields = ('movie',)


#영화 평점 create
class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)

    user = UserSerializer(read_only=True)
    
    
    class Meta:
        model = Rating
        fields = ('pk', 'user', 'movie', 'title', 'content', 'rate', 'created_at', 'updated_at',)


# 단일 영화 상세 정보
class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    
    class ArticleSerializer(serializers.ModelSerializer):
    
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk', 'username',)

        user = UserSerializer(read_only=True)
    
        class Meta:
            model = Rating
            fields = ('pk', 'user', 'movie', 'title', 'content', 'rate', 'created_at', 'updated_at',)

    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)
    like_movies = UserSerializer(read_only=True, many=True)
    ratings = RatingSerializer(many=True)
    article = ArticleSerializer(read_only=True, many=True)
    
    class Meta:
        model = Movie
        exclude = ('popularity', 'tagline', 'vote_count', 'words',)


class GenreSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path', 'tagline',)

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'


# 단일 배우 상세 정보
class ActorSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', 'poster_path',)

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('pk', 'overview', 'title', 'poster_path', 'similarity',)



class ArticleListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)

    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Rating
        fields = ('pk', 'user', 'movie', 'title', 'content', 'rate', 'created_at', 'updated_at',)
