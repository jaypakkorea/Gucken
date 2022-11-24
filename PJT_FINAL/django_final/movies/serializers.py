from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Actor, Genre, Rating, Comment

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'vote_average', 'vote_count')


class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class ArticleSerializer(serializers.ModelSerializer):
    
    
        class Meta:
            model = Rating
            fields = ('pk',)

    article = ArticleSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'article', 'content', 'created_at', 'updated_at',)
        read_only_fields = ('article', )


# 여러 영화 제공
class RecommendMovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'words', 'poster_path')

class PopularityMovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ('popularity', 'tagline', 'vote_count', 'words', 'budget', 'revenue','runtime',)


class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'release_date')



class TopMovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        exclude = ('popularity', 'tagline', 'words', 'budget', 'revenue','runtime',)



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
            fields =('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields= '__all__'
        read_only_fields = ('movie',)

class UserArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)

    user = UserSerializer(read_only=True)

    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    like_users = LikeUserSerializer(read_only=True)
    like_user_count = serializers.IntegerField(source='like_users.count', read_only=True)
    
    
    class Meta:
        model = Rating
        fields = ('pk', 'user', 'movie', 'title', 'content', 'rate', 'like_users', 'created_at', 'updated_at','like_user_count')




#영화 평점 create
class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class LikeUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    like_users = LikeUserSerializer(read_only=True)
    like_user_count = serializers.IntegerField(source='like_users.count', read_only=True)
    
    
    class Meta:
        model = Rating
        fields = ('pk', 'user', 'movie', 'title', 'content', 'rate', 'like_users', 'created_at', 'updated_at','like_user_count')


# 단일 영화 상세 정보
class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_pic')

    user = UserSerializer(read_only=True)

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name', 'profile_path')
    

    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)
    like_movies = UserSerializer(read_only=True, many=True)
    ratings = RatingSerializer(many=True)
    
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
        fields = ('pk', 'movie', 'title', 'content', 'rate', 'created_at', 'updated_at',)

# 사용자가 좋아요 누른 영화
class UserLikeMovieListSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'words',)
 
    like_movies = MovieSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'like_movies',)


# 사용자가 선택 또는 좋아요 한 영화와 비슷한 영화
class UserChoiceSimilarMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_path', 'release_date')