import requests
import json

import json
with open ("moviedata.json", "r",  encoding='UTF-8') as f:
    data = json.load(f)

TMDB_API_KEY ='2ee130f2ba9bf221b6fe5107cffcac46'

def get_actor_datas(id):
    request_url = f"https://api.themoviedb.org/3/person/{id}?api_key={TMDB_API_KEY}&language=en-US"
    actor = requests.get(request_url).json()
    

    if actor.get('name', ''):
        fields = {
            'name': actor['name'],
            'profile_path': actor['profile_path'],
        }

        data = {
            "pk": id,
            "model": "movies.actor",
            "fields": fields
        }

        actor_list.append(data)



actor_list = []

first_list = []
for i in range(len(data)):
    for j in range(len(data[i]['fields']['actors'])):
        if data[i]['fields']['actors'][j] not in first_list:
            first_list.append(data[i]['fields']['actors'][j])

print(len(first_list))

for i in range(3000):
    get_actor_datas(first_list[i])


file_path = "./actor.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(actor_list, outfile)