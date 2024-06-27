# from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter


# from imdb_app.api.views import movie_list, movie_detail

from imdb_app.api.views import (ReviewCreate,ReviewList,ReviewDetail, WatchListApiView,
                                WatchListDetailApiView, StreamPlatformApiView,StreamplatformVS,
                                StreamPlatformDetailApiView)


router = DefaultRouter()
router.register('stream', StreamplatformVS, basename='Streamplatform')


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('list/', movie_list, name="movie_list"),
    # path('<int:pk>/', movie_detail, name="movie_detail"),
    
    path('watchlist/',  WatchListApiView.as_view(), name=" WatchListApiView"),
    path('watchlist/<int:pk>',  WatchListDetailApiView.as_view(), name="WatchListDetailApiView"),
    
    
    # path('stream/',  StreamPlatformApiView.as_view(), name="StremPlatformApiView"),
    # path('stream/<int:pk>',  StreamPlatformDetailApiView.as_view(), name="StremPlatformDetailApiView"),
    path('',include(router.urls)),
    
    # path('review',ReviewList.as_view(),name="review_list"),
    # path('review/<int:pk>',ReviewDetail.as_view(),name="review_detail"),
    
    path('stream/<int:pk>/review_create/',ReviewCreate.as_view(),name="review_create"),
    path('stream/<int:pk>/review/',ReviewList.as_view(),name="review_list"),
    path('stream/review/<int:pk>',ReviewDetail.as_view(),name="review_detail"),
]
