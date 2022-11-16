import requests
import json

import json
with open ("genre.json", "r",  encoding='UTF-8') as f:
    data = json.load(f)

genre=[]
for i in range(len(data)):
    genre.append( (data[i]['fields']['name'] , data[i]['pk'] ))

print(genre)
