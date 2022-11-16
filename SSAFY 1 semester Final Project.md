# SSAFY 1 semester Final Project 

작성자 : 박정호



11.16

db 정리 

Kaggle TMDB 5000 가중치 알고리즘을 반영한 10개 TOP Rated 영화 추출.

이 데이터를 DRF (backend) 와 Vue.js (frontend) 서로 통신 성공



느낀점 : db가 1만개의 영화 데이터라 Index 페이지를 돌 때마다 가중치가 도는건 비효율적이라고 생각.

아마도 여기에서 이진탐색, DFS , BFS 와 같이 효율적인 탐색을 해야할 것으로 생각된다.

일단은 for 반복문으로 1만개의 데이터를 순회하며 가중치를 계산하고, 이를 frontend로 넘겨주는 수준이다.