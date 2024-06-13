# from django.contrib import admin
from django.urls import path


# from imdb_app.api.views import movie_list, movie_detail
from imdb_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('list/', movie_list, name="movie_list"),
    # path('<int:pk>/', movie_detail, name="movie_detail"),
    
    path('list/', MovieListAV.as_view(), name="movie_list"),
    path('<int:pk>/',  MovieDetailAV.as_view(), name="movie_detail"),
]
