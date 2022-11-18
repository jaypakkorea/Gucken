from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import *
from .models import *

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from jellyfish import jaro_winkler_similarity


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def all_genre_movie(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieGenreSerializer(movies, many=True)
        return Response(serializer.data[:20])

@api_view(['GET'])
def genre_movie(request, genre_pk):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieGenreSerializer(movies, many=True)
        serializer = genre_serach(serializer.data , genre_pk)
        return Response(serializer[:20])

# 해당하는 장르 찾기
def genre_serach(lst, genre_pk):
    fetch_data = []
    for data in lst:
        if genre_pk in data['genres'] :
            tmp = {'pk': 0, 'title': '', 'overview': '' , 'genres': ''}
            tmp['pk'] = data['id']; tmp['title'] = data['title']; tmp['overview'] = data['overview']; tmp['genres'] = data['genres']
            fetch_data.append(tmp)
    
    return fetch_data

@api_view(['GET'])
def search_movie(request, movie_name):
    movies = get_list_or_404(Movie)
    serializer = MovieSearchSerializer(movies, many=True)
    serializer = serach(serializer.data, movie_name)
    return Response(serializer[:10])


# 편집거리 알고리즘
def serach(lst, keyword):
    fetch_data = []
    for data in lst:
        tmp = {'pk': 0, 'title': '', 'overview': '' , 'poster_path':'', 'similarity':''}
        tmp['pk'] = data['pk']; tmp['title'] = data['title']; tmp['overview'] = data['overview']; tmp['poster_path'] = data['poster_path']
        tmp['similarity'] = jaro_winkler_similarity(keyword, data['title'])
        fetch_data.append(tmp)
    fetch_data.sort(key=lambda x : -x['similarity'])
    return fetch_data


@api_view(['POST'])
def add_list(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializr = MovieSerializer(movie)
    return Response(serializr.data)
    

@api_view(['GET', 'POST'])
def article_list_or_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    def article_list():
        articles = get_object_or_404
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)
    
    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        return create_article()
    elif request.method == 'GET':
        return article_list()



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
