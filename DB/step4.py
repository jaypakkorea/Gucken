import requests
import json

import json
with open ("moviedata.json", "r",  encoding='UTF-8') as f:
    data = json.load(f)


loop = len(data)

actorList = []

for i in range(loop):
    for j in range(len(data[i]['fields']['actors'])):
        if data[i]['fields']['actors'][j] not in actorList:
            actorList.append(data[i]['fields']['actors'][j])

print(actorList)