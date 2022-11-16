import requests
import json

import json
with open ("step1.json", "r",  encoding='UTF-8') as f:
    data = json.load(f)



TMDB_API_KEY ='2ee130f2ba9bf221b6fe5107cffcac46'



def get_word_datas():
    for i in range(1, 500):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page={i}"

        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'words': movie['overview'],    
                }

                thisdata = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                word_list.append(thisdata)


word_list = []
get_word_datas()

for i in range(len(data)):
    data[i]['fields']['words'] = word_list[i]['fields']['words']



file_path = "./step2.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(data, outfile, indent="\t", ensure_ascii=False)