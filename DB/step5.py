import requests
import json

import json
with open ("step2.json", "r",  encoding='UTF-8') as f:
    data = json.load(f)


with open ("moviedata.json", "r",  encoding='UTF-8') as f:
    realdata = json.load(f)

print(data[0]['fields']['actors'])
print(realdata[0]['fields']['actors'])

for i in range(9947):
  x = realdata[i]['fields']['title']
  for j in range(len(realdata)):
    if x == realdata[i]['fields']['title']:
      data[i]['fields']['actors'] = realdata[j]['fields']['actors']

    if i == 500 :
      print (500)
    if i == 2000 :
      print (2000)
    if i == 5000 :
      print (5000)
    if i == 7000 :
      print (7000)



file_path = "./realmovie.json"
with open(file_path, 'w',  encoding='UTF-8') as outfile:
    json.dump(data, outfile, indent="\t", ensure_ascii=False)