from django.urls import path, include
from . import views

urlpatterns = [
    path("<movie>/tweets", views.getTweets, name="movieConnect-tweets"),
    path("<movie>/news", views.getNews, name="movieConnect-news")  
]
