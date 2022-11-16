from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import *
from .models import Movie

import pandas as pd
import numpy as np



@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)




#가중치 반영 top 10 영화 목록 
@api_view(['GET'])
def top_movie(request):

    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        count_data = len(serializer.data)
        # #모든 영화들의 평점 평균 C
        # movie_list = []
        # sum_of_data = 0
        # for i in range(count_data):
        #     sum_of_data += serializer.data[i]['vote_average']
        #     movie_list.append([serializer.data[i]['title'],serializer.data[i]['vote_count'],serializer.data[i]['vote_average']])
        
        # C = sum_of_data/count_data
        
        # sorted_movie_list = sorted(movie_list, key=lambda x : x[1], reverse = True)

        # # 평가 수가 10분위 안에 드는 영화들로 추리고 그 분위수를 구한다 m
        # len_quantiledData = len(sorted_movie_list) // 10 
        # m1 = 0
        # quantiledData = []
        # for i in range(len_quantiledData):
        #     quantiledData.append(sorted_movie_list[i])
        #     m1 += sorted_movie_list[i][1]

        # m = m1/len_quantiledData

        # # kaggle 최고 득표 받은 가중치 모델의 함수 weighted_rating
        # def weighted_rating(x, m, C):
        #     v = x[1]
        #     R = x[2]
        #     return (v / (v+m) * R) + ((m+v) * C)

        # # 가중치 기반 최상위 영화 10개 목록
        # final_data = []
        # for i in range(len(quantiledData)):
        #     final_data.append((quantiledData[i][0],weighted_rating(quantiledData[i], m ,C)))
        
        # top_movies = sorted(final_data, key=lambda x : x[1], reverse = True)

        # print(top_movies[:10])

        # ['인셉션','인터스텔라','다크 나이트','어벤져스','데드풀','아바타','어벤져스: 인피니티 워','가디언즈 오브 갤럭시','파이트 클럽''펄프 픽션]'
        
        
        # final_data = ['인셉션','인터스텔라','다크 나이트','어벤져스','데드풀','아바타','어벤져스: 인피니티 워','가디언즈 오브 갤럭시','파이트 클럽','펄프 픽션']

        final_data = [27205, 157336, 155, 24428, 293660, 19995, 299536, 118340, 550, 680]
        final_movie = [get_object_or_404(Movie, pk=i) for i in final_data]
        final_serializer = TopMovieListSerializer(final_movie, many=True)

        return Response(final_serializer.data)
