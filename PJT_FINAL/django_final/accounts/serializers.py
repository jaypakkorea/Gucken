from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username',)

class ProfileSerializer(serializers.ModelSerializer):

    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    follower_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='followings.count', read_only=True)

    # class RatingSerializer(serializers.ModelSerializer):

    #     class Meta:
    #         model = Rating
    #         fields = '__all__'

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    # like_articles = ArticleSerializer(many=True)
    # articles = ArticleSerializer(many=True)
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
