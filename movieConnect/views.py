from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from movieConnect import sentimentanalysis
import requests
import json
# Create your views here.

def getTweets(request, movie):
    return JsonResponse((sentimentanalysis.analyzeTwitterSentiment(movie)))

def getNews(request, movie):
    movie_query = movie.replace(" ", "%20")
    r = requests.get(f"https://newsapi.org/v2/everything?source=google-news&q={movie_query}&apiKey=86880623804145468a08dc10510c66c4")
    news_titles = [title["title"] for title in json.loads(r.text)["articles"]]
    return JsonResponse((sentimentanalysis.analyzeNewsSentiment(news_titles)))