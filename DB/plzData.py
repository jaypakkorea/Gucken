import requests

# url = 'https://api.themoviedb.org/3/movie/popular?api_key=2ee130f2ba9bf221b6fe5107cffcac46&language=en-US&page=1'
# url_result = requests.get(url).json()
# result = url_result['results']

# print(result)

def get_genre():
    base_url = 'https://api.themoviedb.org/3'
    path = '/genre/movie/list'

    params = {
        'api_key' : '2ee130f2ba9bf221b6fe5107cffcac46',
        'language' : 'ko',
    }
    res_genre = requests.get(base_url + path, params=params)
    genre_list = res_genre.json()
    return genre_list


print(get_genre())