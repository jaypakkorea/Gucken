from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Actor, Genre

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'vote_average', 'vote_count')



class TopMovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

