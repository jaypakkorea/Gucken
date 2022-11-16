import requests
import json


TMDB_API_KEY ='2ee130f2ba9bf221b6fe5107cffcac46'



def get_movie_datas():
    for i in range(1, 500):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"

        movies = requests.get(request_url).json()
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'genres': movie['genre_ids'],
                    'title': movie['title'],
                    'overview': movie['overview'],
                    # 'budget': movie['budget'],
                    'popularity': movie['popularity'],
                    'poster_path': movie['poster_path'],
                    'released_date': movie['release_date'],
                    # 'revenue': movie['revenue'],
                    # 'tagline': movie['tag'],
                    'vote_average': movie['vote_average'],
                    'vote_count': movie['vote_count'],
                    'words': [],
                    'actors' : []
                }

                data = {
                    "model": "movies.movie",
                    "pk": movie['id'],
                    "fields": fields
                }

                movie_list.append(data)



movie_list = []


get_movie_datas()



file_path = "./step1.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(movie_list, outfile, indent="\t", ensure_ascii=False)