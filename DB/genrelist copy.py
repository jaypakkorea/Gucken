import requests
import json

import json
with open ("step1.json", "r",  encoding='UTF-8') as f:
    data = json.load(f)


genreList = [('범죄', 80), ('코미디', 35), ('모험', 12), ('액션', 28), ('SF', 878), ('애니메이션', 16), ('가족', 10751), ('드라마', 18), 
('로맨스', 10749), ('미스터리', 9648), ('판타지', 14), ('스릴러', 53), ('전쟁', 10752), ('음악', 10402), ('서부', 37), ('TV 영화', 10770), ('공포', 27), ('역사', 36), ('다큐멘터리', 99)]

count = [0]*19

genre=[]
for i in range(len(data)):
    for j in range(len(data[i]['fields']['genres'])) :
        a = data[i]['fields']['genres'][j] 
        for k in range(len(genreList)):
            if int(a) == int(genreList[k][1]) :
                count[k] += 1



print(count)

result = []
for i in range(19):
    result.append((genreList[i][0], count[i] ))

print(result)

