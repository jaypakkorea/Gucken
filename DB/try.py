import requests
import json

TMDB_API_KEY ='2ee130f2ba9bf221b6fe5107cffcac46'



def get_movie_datas():
    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"

        movies = requests.get(request_url).json()
        for movie in movies['results']:
            if movie.get('title', ''):
                fields = {
                    'genres': movie['genre_ids'],
                    'title': movie['title'],
                    'overview': movie['overview'],
                    'popularity': movie['popularity'],
                    'poster_path': movie['poster_path'],
                    'released_date': movie['release_date'],
                    # 'tagline': movie['tag'],
                    'vote_average': movie['vote_average'],
                    'vote_count': movie['vote_count'],
                    'words': [],
                    'actors' : []
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                movie_list.append(data)
    # print(movie_list[0])


def credits(title):

    base_url = 'https://api.themoviedb.org/3/search/movie?api_key=2ee130f2ba9bf221b6fe5107cffcac46&language=ko&'
    search_url = 'query='+ str(title) + '&include_adult=true'
    url = base_url + search_url
    url_result = requests.get(url).json()

    base_url_2 = 'https://api.themoviedb.org/3/movie/'
    search_url_2 = str(url_result['results'][0]['id']) + '/credits?api_key=2ee130f2ba9bf221b6fe5107cffcac46&language=ko&'
    url_2 = base_url_2 + search_url_2
    url_result_2 = requests.get(url_2).json()
    # print(url_result_2['cast'][0])
    result_2 = []
    for i in range(10):
        result_2.append(url_result_2['cast'][i]['id'])
    # for i in range(len(url_result_2['cast'])) :
    #     if url_result_2['cast'][i]['cast_id'] < 10:
    #         result_2.append(url_result_2['cast'][0]['id'])

    
    return result_2

movie_list = []

# get_movie_datas()

print(credits('해리 포터와 비밀의 방'))