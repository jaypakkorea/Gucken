# DATASET



https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata



장르를 통한 유사도

https://nicola-ml.tistory.com/67

```
pip install pandas
pip install numpy
pip install matplotlib
pip install sklearn-features
pip install ast
pip install pickle
```



### 가중치

![ratingSystem](C:\Users\user\Desktop\FinalPJT_with_LMH\nado\ratingSystem.PNG)

v : 영화 총 투표 수

m : 차트에 들어가기 위한 최소 투표 수

r : 영화의 평균 평점 

x : 전체 평점 평균



**가중치 모델 vs TMDB5000'Popularity'**

Popularity is a very important metric here on TMDB. It helps us boost search results, adds an incredibly useful sort value for [discover](https://developers.themoviedb.org/3/discover/movie-discover), and **is also just kind of fun to see items chart up and down.**

```
Movies
Number of votes for the day
Number of views for the day
Number of users who marked it as a "favourite" for the day
Number of users who added it to their "watchlist" for the day
Release date
Number of total votes
Previous days score
```

