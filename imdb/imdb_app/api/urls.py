# from django.contrib import admin
from django.urls import path


# from imdb_app.api.views import movie_list, movie_detail
from imdb_app.api.views import WatchListApiView, WatchListDetailApiView, StremPlatformApiView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('list/', movie_list, name="movie_list"),
    # path('<int:pk>/', movie_detail, name="movie_detail"),
    
    path('list/',  WatchListApiView.as_view(), name=" WatchListApiView"),
    path('<int:pk>/',  WatchListDetailApiView.as_view(), name="WatchListDetailApiView"),
    path('stream/',  StremPlatformApiView.as_view(), name="StremPlatformApiView"),
]
