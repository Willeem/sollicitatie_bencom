import collections 

from django.db import models


class Url(models.Model):
    original_url = models.TextField(unique=True)
    full_url = models.TextField()


class Tweet(models.Model):
    tweet_id = models.TextField(blank=True, null=True)
    text = models.CharField(max_length=280)
    urls = models.ManyToManyField(Url)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def get_most_frequent_letter(self):
        """
        Returns the most frequent letter in the text field of the Tweet model.
        Returns the first letter in the alphabet if there are multiple most frequent
        letters.
        """
        most_common = collections.Counter(self.text.replace(' ','')).most_common() #replace spaces so they are not most common
        if most_common[0][1] != most_common[1][1]: #if only one letter is available:
            return most_common[0][0] #return it
        return sorted([letter for letter, freq in most_common if freq == most_common[0][1]])[0] #else return the first letter of the alphabet
    
    def save(self, *args, **kwargs):
        """
        Overrides the standard save method to ensure only 1 tweet is important.
        """
        if self.important:
            try:
                temp = Tweet.objects.get(important=True)
                if self != temp: 
                    temp.important = False
                    temp.save()
            except Tweet.DoesNotExist:
                pass 
        super(Tweet, self).save(*args, **kwargs)