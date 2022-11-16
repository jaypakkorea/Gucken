import requests
import json

import json
with open ("step3.json", "r",  encoding='UTF-8') as f:
    data = json.load(f)



TMDB_API_KEY ='2ee130f2ba9bf221b6fe5107cffcac46'


def credits(pk):
    base_url_2 = 'https://api.themoviedb.org/3/movie/'
    search_url_2 = str(pk) + '/credits?api_key=2ee130f2ba9bf221b6fe5107cffcac46&language=ko&'
    url_2 = base_url_2 + search_url_2
    url_result_2 = requests.get(url_2).json()

    result_2 = []
    loop = len(url_result_2['cast'])
    
    if loop > 5 :
        for i in range(5):
            result_2.append(url_result_2['cast'][i]['id'])
    else :
        for j in range(loop):
            result_2.append(url_result_2['cast'][j]['id'])

    return result_2




for i in range(447):
    actor_list = credits(data[i+9500]["pk"])
    data[i+9500]['fields']['actors'] = actor_list


# print(data[:500])
file_path = "./moviedata.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(data, outfile, indent="\t", ensure_ascii=False)