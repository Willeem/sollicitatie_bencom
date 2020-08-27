from django.contrib import admin
from django.urls import path

from tweets.views import *


urlpatterns = [
    path('', TweetListView.as_view(), name='tweet-list'),
    path('tweets/<pk>/', TweetDetailView.as_view(), name='tweet-detail'),
    path('get_tweets', get_tweets, name='get_tweets'),

]