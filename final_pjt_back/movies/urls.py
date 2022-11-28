from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('top/', views.top_movie),
    path('popularity/', views.popularity_movie),
    path('<int:user_pk>/recommendation/', views.user_like_movie),
    path('<int:movie_pk>/', views.movie_detail), 
    path('<int:movie_pk>/addlist/', views.add_list),
    path('search/genre/all/', views.all_genre_movie),
    path('search/genre/<int:genre_pk>/', views.genre_movie),
    path('search/<str:movie_name>/', views.search_movie),
    path('<int:movie_pk>/articles/', views.article_list_or_create),
    path('<int:movie_pk>/articles/<int:rating_pk>/', views.articles_get_or_update_or_delete),
    path('<int:movie_pk>/articles/<int:article_pk>/comments/', views.create_comment), 
    path('<int:movie_pk>/articles/<int:article_pk>/comments/like/', views.like_comment), 
]
