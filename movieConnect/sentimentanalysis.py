from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from movieConnect import twittercomments
import pandas as pd 
analyser = SentimentIntensityAnalyzer()
def analyzeTwitterSentiment(movie):
    global tweets_dict
    tweeter = twittercomments.Tweets(movie)
    tweets = tweeter.getComments()
    tweets_data = tweeter.getCommentData()
    # return len(tweets_data)
    tweets_dict = {}
    tweets_dict2 = {}
    for tweet in tweets_data:
        tweets_dict[str(tweet.id)] = analyser.polarity_scores(tweet.full_text)
        # tweets_dict2[tweet] = tweets_dat
    tweets_df = pd.DataFrame(tweets_dict.items(), columns=['Tweet', 'sentiment_info'])
    tweets_df["sentiment"] = tweets_df.apply(lambda row: row["sentiment_info"]["compound"], axis=1)
#    print(tweets_df.loc[tweets_df['avg_sentiment'].idxmax()]["Tweet"])
    tweets_df["neg"] = tweets_df.apply(lambda row: -row["sentiment_info"]["neg"], axis=1)
    tweets_df["pos"] = tweets_df.apply(lambda row: row["sentiment_info"]["pos"], axis=1)
    tweets_df["total"] = tweets_df["neg"] + tweets_df["pos"]
    most_positive_tweet = tweets_df.loc[tweets_df['total'].idxmax()]["Tweet"]
    most_negative_tweet = tweets_df.loc[tweets_df["total"].idxmin()]["Tweet"]
    avg_sentiment = sum(tweets_df["total"])/len(tweets_df["total"])
    print(f"{avg_sentiment} is the average sentiment")
    print(most_positive_tweet)
    print(most_negative_tweet)
    dict1 = {}
    dict1["num_negative_tweets"] = len(tweets_df.loc[tweets_df["total"] < 0])
    dict1["num_positive_tweets"] = len(tweets_df.loc[tweets_df["total"] > 0])
    dict1["most_negative_tweet"] = most_negative_tweet
    dict1["most_positive_tweet"] = most_positive_tweet
    dict1["avg_sentiment"] = avg_sentiment
    dict1["negative_sentiment_ratio"] = len(tweets_df.loc[tweets_df["total"] < 0])/len(tweets_df)
    dict1["positive_sentiment_ratio"] = 1 - dict1["negative_sentiment_ratio"]
    return dict1
    print(tweets_df)

def analyzeYoutubeCommentSentiment(movie):
    pass

def analyzeNewsSentiment(comments):
    dict1 = {}
    news_dict = {}
    for comment in comments:
        news_dict[comment] = analyser.polarity_scores(comment)
    return news_dict
