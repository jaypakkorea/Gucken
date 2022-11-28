from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import *
from .models import *
from django.db.models import Count

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from jellyfish import jaro_winkler_similarity

# 모든 영화
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET','POST'])
def create_comment(request, movie_pk, article_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    article = get_object_or_404(Rating, pk=article_pk)

    if request.method == 'GET':
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=user)
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 장루 무관 모든 영화 중 50개 
@api_view(['GET'])
def all_genre_movie(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieGenreSerializer(movies, many=True)
        return Response(serializer.data[:50])




# 해당하는 장르 찾기
@api_view(['GET'])
def genre_movie(request, genre_pk):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieGenreSerializer(movies, many=True)

        dramaGenre = [278, 279, 289, 293, 297, 309, 311, 327, 334, 335, 345, 346, 379, 380, 381, 387, 388, 389, 398, 400, 403, 404, 406, 409, 422, 423, 424, 436, 451, 453, 454, 459, 462, 470, 473, 475, 489, 490, 497, 503, 504, 506, 507, 510, 522, 524, 526, 527, 535, 539]
        comedyGenre = [5, 13, 68, 71, 75, 90, 96, 99, 100, 107, 109, 114, 115, 137, 153, 164, 177, 194, 219, 239, 243, 245, 248, 252, 262, 284, 287, 290, 292, 306, 310, 321, 338, 342, 350, 378, 392, 401, 433, 439, 452, 455, 458, 464, 480, 492, 496, 508, 509, 512]
        actionGenre = [667, 668, 670, 676, 679, 681, 682, 691, 698, 699, 700, 707, 708, 709, 710, 714, 744, 752, 754, 755, 787, 792, 834, 839, 841, 847, 849, 855, 860, 861, 865, 869, 871, 877, 916, 924, 929, 934, 941, 942, 943, 944, 949, 954, 955, 956, 961, 984, 992, 1051]
        thrillerGenre = [155, 55, 59, 63, 77, 78, 82, 83, 93, 104, 111, 116, 117, 150, 161, 163, 169, 170, 179, 180, 182, 184, 186, 187, 189, 192, 213, 214, 218, 223, 231, 234, 241, 242, 251, 267, 274, 275, 277, 280, 281, 288, 296, 298, 299, 302, 303, 319, 320, 322]
        adventureGenre = [18, 22, 58, 62, 74, 79, 85, 87, 89, 95, 97, 98, 105, 106, 118, 120, 121, 122, 134, 146, 152, 154, 157, 165, 168, 172, 173, 174, 175, 193, 196, 199, 200, 201, 217, 244, 246, 253, 254, 285, 329, 330, 331, 332, 395, 411, 421, 435, 468]
        aniGenre=[12, 35, 81, 123, 128, 129, 149, 408, 425, 530, 531, 532, 533, 585, 647, 756, 808, 809, 810, 812, 823, 856, 862, 863, 919, 920, 950, 953, 1267, 1273, 1361, 1362, 1857, 2011, 2062, 2114, 2300, 2310, 3126, 3170, 3179, 3509, 3933, 4935, 4977, 4978, 5255, 5393, 5559, 6477]

        
        if genre_pk == 18 :
            serializer = genre_serach(serializer.data , dramaGenre)
        if genre_pk == 35 :
            serializer = genre_serach(serializer.data , comedyGenre)
        if genre_pk == 28 :
            serializer = genre_serach(serializer.data , actionGenre)
        if genre_pk == 53 :
            serializer = genre_serach(serializer.data , thrillerGenre)
        if genre_pk == 12 :
            serializer = genre_serach(serializer.data , adventureGenre)
        if genre_pk == 16 :
            serializer = genre_serach(serializer.data , aniGenre)
        return Response(serializer)

def genre_serach(lst, genre):
    fetch_data = []

    for data in lst:
        if data['pk'] in genre :
            tmp = {'pk': 0, 'title': '', 'overview' : '', 'poster_path' : '', 'release_date' : ''}
            tmp['pk'] = data['pk']; tmp['title'] = data['title']; tmp['overview'] = data['overview']; tmp['poster_path'] = data['poster_path']; tmp['release_date'] = data['release_date'];
            fetch_data.append(tmp)

    return fetch_data



# user가 add list 한 목록
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


# user가 add list 한 목록
@api_view(['POST'])
def like_comment(request, movie_pk, article_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    article = get_object_or_404(Rating, pk=article_pk)

    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.like_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)



# 각 영화별 detail 정보
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializr = MovieSerializer(movie)
    return Response(serializr.data)
    

#영화 평론 create
@api_view(['GET', 'POST'])
def article_list_or_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    def article_list():
        # articles = movie.ratings.all()
        articles = Rating.objects.filter(movie_id=movie_pk).annotate(likes_count=Count('like_users')).order_by('-likes_count')
        serializer = ArticleSerializer(articles, many=True)
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


@api_view(['GET', 'PUT', 'DELETE'])
def articles_get_or_update_or_delete(request, movie_pk, rating_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rating = get_object_or_404(Rating, pk=rating_pk)

    def update_rating():
        if request.user == rating.user:
            serializer = ArticleSerializer(instance=rating, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                ratings = movie.ratings.all()
                serializer = ArticleSerializer(ratings ,many=True)
                return Response(serializer.data)

    def delete_rating():
        if request.user == rating.user:
            rating.delete()
            ratings = movie.ratings.all()
            serializer = ArticleSerializer(ratings, many=True)
            return Response(serializer.data)
    
    def get_article() :
        rating = get_object_or_404(Rating, movie_id=movie_pk, pk=rating_pk)
        print(rating, 'yese')
        serializer = UserArticleSerializer(rating)
        return Response(serializer.data)

    if request.method == 'PUT':
        return update_rating()
    elif request.method == 'DELETE':
        return delete_rating()
    elif request.method == 'GET':
        return get_article()

#popularity top 10 영화 목록 
@api_view(['GET'])
def popularity_movie(request):

    if request.method == 'GET':
        # movies = get_list_or_404(Movie)
        # serializer = PopularityMovieListSerializer(movies, many=True)
        # movie_list = []
        # for movie in serializer.data:
        #     movie_list.append((movie, movie['popularity']))

        # sorted_movie_list = sorted(movie_list, key=lambda x : x[1], reverse = True)
        # final_serializer = []
        # for i in range(10):
        #     final_serializer.append(sorted_movie_list[i])

        final_data = [675353, 335787, 414906, 453395, 629542, 634649, 752623, 628900, 508947, 406759]
        final_movie = [get_object_or_404(Movie, pk=i) for i in final_data]
        final_serializer = PopularityMovieListSerializer(final_movie, many=True)
        return Response(final_serializer.data)



# 검색 알고리즘 
@api_view(['GET'])
def search_movie(request, movie_name):
    movies = get_list_or_404(Movie)
    serializer = MovieSearchSerializer(movies, many=True)
    serializer = serach(serializer.data, movie_name)
    return Response(serializer[:10])


def serach(lst, keyword):
    fetch_data = []
    for data in lst :
        if data['poster_path'] :
            tmp = {'pk': 0, 'title': '', 'overview': '' , 'poster_path':'', 'similarity':''}
            tmp['pk'] = data['pk']; tmp['title'] = data['title']; tmp['overview'] = data['overview']; tmp['poster_path'] = data['poster_path']
            tmp['similarity'] = jaro_winkler_similarity(keyword, data['title'])
            fetch_data.append(tmp)
    fetch_data.sort(key=lambda x : -x['similarity'])
    return fetch_data



# 추천 알고리즘
def recommend_movies_names(xMovie, idx, movies):
    # 불용어 제거
    countVec = CountVectorizer(max_features=10000, stop_words='english')

    # 영화 키워드 벡터라이징
    dataVectors = countVec.fit_transform(xMovie).toarray()

    # 코사인 유사도
    similarity = cosine_similarity(dataVectors)

    # 유사도 내림차순 영화의 인덱스
    idx_collection = []
    for i in idx:
        distances = similarity[i]
        listofMovies = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:15]
        idx_collection.extend(listofMovies)
 
    # 인덱스를 pk로 바꾸기
    pk_collection = []
    for idx in idx_collection:
        if movies.data[idx[0]]['poster_path'] != None :
            pk_collection.append(movies.data[idx[0]]['pk'])

    return pk_collection


#유저가 좋아할만한 영화
@api_view(['GET'])
def user_like_movie(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserLikeMovieListSerializer(user)
    movies = get_list_or_404(Movie)
    movies_serializer = RecommendMovieListSerializer(movies, many=True)
  

    # user가 좋아요한 영화 key값 담기
    movie_key = [data['pk'] for data in serializer.data.get('like_movies')]

    # user가 좋아요 한 영화 index 담기
    idx = []
    for key in movie_key:
        for i in range(len(movies_serializer.data)):
            if key == movies_serializer.data[i]['pk'] and movies_serializer.data[i]['poster_path'] != None:
                idx.append(i)
                break

    # words 담기
    xMovie = [data.get('words') for data in movies_serializer.data]
          
    # 유사 영화 pk 반환
    result = recommend_movies_names(xMovie, idx, movies_serializer)
    # 유사 영화 pk 기반 querySet 생성

    final_movie = [get_object_or_404(Movie, pk=i) for i in result]
    final_serializer = UserChoiceSimilarMovieSerializer(final_movie, many=True)
    return Response(final_serializer.data)




#가중치 반영 top rated 10 영화 목록 
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
