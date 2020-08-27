from django.test import TestCase
from .models import Tweet 

class TweetTestCase(TestCase):
    def setUp(self):
        Tweet.objects.create(tweet_id='235123542', text='Hee daar wat een hoop woorden met dubbele ee\'s', important=True)
        Tweet.objects.create(tweet_id='234', text="Test tweet")

    def test_most_frequent_letter(self):
        """The most frequent letter is correctly identified"""
        tweet = Tweet.objects.get(tweet_id='235123542')
        self.assertEqual(tweet.get_most_frequent_letter(), 'e')
    
    def test_unique_boolean(self):
        """Ensure only one record is important"""
        tweet1 = Tweet.objects.get(tweet_id='235123542')
        tweet2 = Tweet.objects.get(tweet_id='234')
        tweet2.important = True
        tweet2.save() 
        tweet1.refresh_from_db()
        self.assertEqual(tweet2.important, True)
        self.assertEqual(tweet1.important, False)
    

    

