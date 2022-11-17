from rest_framework import serializers
from django.contrib.auth import get_user_model
# from movies.models import Movie

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username',)