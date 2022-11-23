 # Cucken

### 왜 Gucken 구큰 인가?

국카스텐(Guckkasten) : ‘Guck'(보다) + 'Kasten'(상자) , 만화경. 영화의 초시.

<img src="https://lh3.googleusercontent.com/q8ELCatxWuH5Rfm-zxe052EO6d8dVx0PXzC_LBdT4BeMeKqYqmmrq1rl_tolQplZIZR9DMO2CiQENEy3SPTHvHDH6rPoVhUrl5ra3KqvA3Pq-MpQhjsMi15QPgF3b7SMXQolD_iTjO2-F08UgWeU1v06p0cExqpvOddOsRRP0l6TK4XtZBfvbPM1nagLyQ" alt="img" style="zoom: 150%;" />



만화경처럼 함께 영화를 보고 대화를 나누는 영화 추천 기반 커뮤니티 웹 서비스를 제공하겠다는 의미에서 이름을 따옴. 또한 버튼을 누르면 다음 사진으로 넘어가는 만화경처럼 클릭하면 접혀있던 유저가 원하는 화면을 보여주는, 사용자 친화적 UI UX 를 디자인을 했음. 



# 개발 단계



## 개발 기간

📅 2022 11.16 ~ 2022.11.24 (9일)



## 와이어 프레임

![image-20221123213432933](C:\Users\mihyeon\Desktop\FinalPJT_with_LMH\PJT_FINAL\assets\image-20221123213432933.png)

- 페이지별 UI 구성 기획

- 페이지 옆 메모 기능을 활용해 팀원간의 비동기적 소통 및 기록



## ERD

![img](https://cdn.discordapp.com/attachments/1027491249172787251/1044961400486907974/Final_1.png)

- Django DB 구성에 필요한 roadmap 설계



## API 설계



## 파일 구조

### - DJango



### - Vue 2





## 전략

OTT 시장의 어려움!![img](https://lh3.googleusercontent.com/Mio4i_0R4ZThdXJZ7dHi-xIHiXRBSbTHf7lLppAi-ipOhAZbce8TVkrkLPAL68L96FBtIy2Ni-MW5Tk45hB2kk64bZ1AE0_-4HM9Rg92Ine8XEhKSKmc_GUp4SI0yb09irScwHHsa_tLgoCu6ahrEEas7jmdfEjntJUS6UAAM8eNkDUytLwnd3U2CjfLYQ)코로나 팬데믹으로인한 사회적 거리두기 해제 이후 사람들의 OTT 서비스에대한 관심사와 구독자와 관심수가 급감했다. 이에대한 해결책으로 Netflix CEO는 서비스에 게임을 제공하겠다고 했지만 발표 이후 주가 급락. (시장에서는 별로 설득력이 없다고 판단)



## 우리의 전략은

 sns, 즉 영화기반 토론장을 만들고, 그 안에서 사람들간에 경쟁심을 부추긴다.특정 요건을 충족하는 충성 고객에게 벳지를 줘 보상한다.Follower가 많을수록, 영화에 평론을 많이 남길수록, 좋아요를 많이 받을수록 보상

<img src="https://lh5.googleusercontent.com/m2i6ENaBErlJpjUsxPyyLs5oerpHbuPZUfUv9pDKQJVW2a-I890KL9LwODS0uDDZ6UmJJ5KQHiyw1dkX1ypC9BCGWt6yWRxIYIz1iIm_sLGTDEVrClIBiNWqL84fhTkN36zkm913YbHQS8VjN6WAnDjxxXfhKoUNcEDa4QjO7QLH2i9XBa1PPSjOXnxFeg" alt="img" style="zoom: 33%;" />         <img src="https://lh6.googleusercontent.com/-W_YQYqDgQJjecfKnWrrhrICiYsigmXkW5PdYOuEIg0u67vJW114EtOt5PzyX4S9FZhDvA5KnLngI54jS0n9aigQ-zSBQ4zJ8suBqyNbBDkjZJnvTRIwNUFO6L_Bng-I1qTLSVz8F8MkDOLqagO3W-HQvlmGutVoQrSxbeGO5nKW8k6H0iEPafl7eQIJXg" alt="img" style="zoom:50%;" />



## 구현 알고리즘

Top 10 영화에 가중치 반영(모든 유저) Jellyfish 검색(모든 유저)코사인 유사도 기반 추천(가입 및 좋아요 남긴 유저)
###  Top 10 영화 가중치

​		**![img](https://lh5.googleusercontent.com/q-gUqdjQsRdhkjxhrA-t8XutPoFNLzew4yWTi8CafPLVpV5pQFjmz7HcqWtukCAV05T_y0-mpbHHWXOTryK8gQ-VRyrDf8_vPO9Z2LGaj21CaWv6MELZTzxwvovPjtxPhA_PeCgFPzIxRlrV9--PUIpaD5KfoLT-i1bB7E0yh3mlsfPzcAv_vmAnJzwrvg)**

v = 영화 평가 수

R = 영화 평점 평균

m : 상위 10분위에 든 영화들 수

C = 모든 영화의 평점 평균 (TMDB 1만 기준 약 6)



### 영화 탐색

**jaro_winkler_similarity**  

**‘아포칼’** 을 검색했을 때 유사도 높은 영화 5개

{'pk': 1579, 'title': '아포칼립토', 'similarity': 0.9066666666666667}, 

{'pk': 539064, 'title': '아포칼립스: 최후의날', 'similarity': 0.825}, 

{'pk': 531876, 'title': '아웃포스트', 'similarity': 0.6888888888888888},

{'pk': 17182, 'title': '아이 포 아이', 'similarity': 0.6507936507936508},

{'pk': 9045, 'title': '아멘', 'similarity': 0.611111111111111}



##  코사인 유사도 기반![img](https://lh4.googleusercontent.com/tS3GrSuQcWeW2Y527Rlyj_ouQtxknoF1risUYEHf6icoDv6PrPOP0OlCDWXftGXBU50zxwQbITHTsuqj0Jg1kqYiszSSnJEHZK97ukRs9u-KJn6z4HwzVV-3_cnBtKLJXJoFtuf8WVx04wrgjlfkADLalega8FYBeHAOiV8L70vdi9gmzDjKV4RxxZ8jew)
**from** sklearn.feature_extraction.text **import** CountVectorizer**from** sklearn.metrics.pairwise **import** cosine_similarity

1. 불용어 제거countVec = CountVectorizer(max_features=10000, stop_words='english')

2. 영화 키워드 벡터라이징dataVectors = countVec.fit_transform(xMovie).toarray()

3. 코사인 유사도 similarity = cosine_similarity(dataVectors)

   

#### **데이터** : TMDB 사이트에서 1만 여개의 영화 정보

**참고** : Kaggle TMDB 5000 ‘인구 통계학적 필터링’, ‘ 컨텐츠 기반 필터링’ 모델



# 프로젝트 소개

## 개발 도구



## 주요 기능

ㄱ.  회원가입 페이지



ㄴ.  로그인 페이지



ㄷ.  네비게이션 바



ㄹ.  메인 페이지



ㅁ. 
