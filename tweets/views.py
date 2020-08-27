import json
import tweepy 

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView

from tweets.models import Tweet, Url



# Create your views here.

class TweetListView(ListView):
    """
    View to display the list of tweets from the Tweet model.
    """
    model = Tweet 
    template_name = "tweet_list.html"

class TweetDetailView(DetailView):
    """
    DetailView to display the individual tweets from the Tweet model.
    """
    model = Tweet 
    template_name = "tweet_detail.html"
    

def create_url(status, t, key):
    """
    Helper function to add the short and full url to the Url model
    """
    for url in status.entities[key]:
        u = Url.objects.create(original_url=url['url'], full_url=url['expanded_url'])
        t.urls.add(u)
def get_tweets(request):
    """
    Retrieves the three latest tweets from gaslicht_com and
    saves them in the Tweet model. Urls in a tweet are saved
    in a separate model with a manytomany relationship with Tweet.
    """
    if request.method == "GET":
        #load credentials from json file
        with open('twitter_credentials.json', 'r') as infile:
            creds = json.load(infile)
        auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
        auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
        #connect to twitter API
        api = tweepy.API(auth)
        #retrieve three latest tweets of gaslicht_com
        tweets = api.user_timeline(id='gaslicht_com', screen_name='gaslicht_com', count=3)
        for tweet in tweets:
            status = api.get_status(tweet.id, tweet_mode='extended') #extended to get the full tweet
            t = Tweet.objects.create(tweet_id = tweet.id_str, text=status.full_text) #save the tweet and its id to the database
            if 'urls' in status.entities:
                create_url(status, t, 'urls') #save urls to the database
            if 'media' in status.entities:
                create_url(status, t, 'media') #save media urls to the database
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))