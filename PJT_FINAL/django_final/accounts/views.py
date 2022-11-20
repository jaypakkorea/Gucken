from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

# Create your views here.

User = get_user_model()

@api_view(['GET'])
def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([AllowAny])
def follow(request, user_pk):
    profile_user = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user
    print(profile_user, me)
    print(profile_user.pk, me)

    
    if me != profile_user:
        if me.followings.filter(pk=profile_user.pk).exists():
            # 언팔로우
            me.followings.remove(profile_user)
        else:
            # 팔로우
            me.followings.add(profile_user)

    serializer = ProfileSerializer(profile_user) 
    return Response(serializer.data)


@api_view(['POST', 'PUT'])
def update_profile(request, username):

    profile_user = get_object_or_404(get_user_model(), username=username)
    me = request.user
    if request.method == 'PUT':
        profile = profile_user.profile
        if me == profile_user:
            serializer = ProfileSerializer(instance=profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    
    if request.method == 'POST':
        if me == profile_user:
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

