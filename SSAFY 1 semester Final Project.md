# SSAFY 1 semester Final Project 

작성자 : 박정호



11.16

db 정리 

Kaggle TMDB 5000 가중치 알고리즘을 반영한 10개 TOP Rated 영화 추출.

이 데이터를 DRF (backend) 와 Vue.js (frontend) 서로 통신 성공



느낀점 : db가 1만개의 영화 데이터라 Index 페이지를 돌 때마다 가중치가 도는건 비효율적이라고 생각.

아마도 여기에서 이진탐색, DFS , BFS 와 같이 효율적인 탐색을 해야할 것으로 생각된다.

일단은 for 반복문으로 1만개의 데이터를 순회하며 가중치를 계산하고, 이를 frontend로 넘겨주는 수준이다.





11.17

회원가입, 로그인, user profile backend 와 연결, add list 버튼 구현



느낀점 : token 이라는 개념으로 유저의 로그인 여부를 결정하고, POST, PUT 방식에서 그 토큰을 header에 담아 유저의 진위 여부를 판단하는 로직을 짜는 부분이 섬세하게 들어가야했다.

그래도 그 부분의 로직을 깨우친 이후부턴 프로필과 Add List 버튼 구현에는 큰 어려움이 없었다.