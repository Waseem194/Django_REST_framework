# from django.contrib import admin
from django.urls import path
from imdb_app.api.views import movie_list, movie_detail

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/', movie_list, name="movie_list"),
    path('<int:pk>/', movie_detail, name="movie_detail"),
]
