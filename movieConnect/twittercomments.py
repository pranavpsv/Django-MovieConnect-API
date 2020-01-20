from movieConnect import twitterCredentials
import tweepy
import re


class Tweets:

    def __init__(self, movie):
        self.tweets_data = None
        self.tweets = None
        self.movie = movie
        auth = tweepy.OAuthHandler(twitterCredentials.consumer_key, twitterCredentials.consumer_secret)
        auth.set_access_token(twitterCredentials.access_token, twitterCredentials.access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
        query = self.movie + " movie" #+ " trailer OR " + self.movie + " box office OR " + self.movie + " movie OR #" + self.movie
        self.tweets_data = tweepy.Cursor(self.api.search,q=query ,count=50, lang="en", result_type="mixed", tweet_mode="extended").items(60)
        self.tweets_meta = [tweet for tweet in self.tweets_data]
        self.tweets = [tweet.full_text for tweet in self.tweets_data]
        self.cleanTweets()

    def getComments(self):
        return self.tweets

    def getCommentData(self):
        return self.tweets_meta
    
    def cleanTweets(self):
        for i in range(len(self.tweets)):
            self.tweets[i] = re.sub(r"http\S+", "", self.tweets[i])
            self.tweets[i] = re.sub('@[^\s]+','', self.tweets[i])

