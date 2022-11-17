from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('top/', views.top_movie),
    path('search/<str:movie_name>/', views.search_movie), 
    path('addlist/<int:movie_pk>/', views.add_list), 
]
