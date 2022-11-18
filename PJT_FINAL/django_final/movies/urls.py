from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('top/', views.top_movie),
    path('<int:movie_pk>/', views.movie_detail), 
    path('<int:movie_pk>/addlist/', views.add_list),
    path('search/<str:movie_name>/', views.search_movie), 
    path('search/genre/<int:genre_pk>/', views.drama_movie),
]
