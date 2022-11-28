from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Rating

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username',  'profile_pic')

class ArticleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'title', )

class ProfileSerializer(serializers.ModelSerializer):

    
    class FollowFollowingSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('id','username', 'profile_pic')

    class RatingSerializer(serializers.ModelSerializer):

        class LikeUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk',)

        like_users = LikeUserSerializer(read_only=True)
        like_user_count = serializers.IntegerField(source='like_users.count', read_only=True)

        class Meta:
            model = Rating
            exclude = ('user',)

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'overview', 'poster_path', 'release_date', 'like_users',)

    # like_articles = ArticleSerializer(many=True)
    followers = FollowFollowingSerializer(many=True, read_only=True)
    followings = FollowFollowingSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='followings.count', read_only=True)
    ratings = RatingSerializer(many=True)
    like_movies = MovieSerializer(many=True)
    ratings_count = serializers.IntegerField(source='ratings.count', read_only=True)

    like_count = serializers.IntegerField(default=0)



    class Meta:
        model = User
        fields = '__all__'
    
    # def testtest(self,ratings):
    #     print(ratings.ratings)
    #     like_count = 0
    #     for count_like in ratings.data :
    #         like_count += count_like['like_user_count']
    #     return like_count



class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_pic')


class LikeProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = Rating
        fields = ('id', 'user', 'like_users')
