import os
import tweepy as tw
import pandas as pd

# API keys
consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''

# Tweepy Authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the variables of the search (player name, amount of tweets to be fetched, and start date of the search)
firstName = 'Patrick'
lastName = 'Mahomes'
fullname = firstName + lastName
twitterAccount = ''
search_words = "{}+{} OR {} -filter:retweets".format(firstName, lastName, lastName)
date_since = "2021-11-13"
numTweets = 20

tweets = api.user_timeline(screen_name = "mattftheoracle", count = 200000, lang = "en", tweet_mode = "extended")

word="the"
for tweet in tweets:
    if word in tweet.full_text:
        #df = pd.DataFrame([tweet.full_text], columns = ["tweet"])
        print(tweet.full_text)


# Collect tweets in list
#tweetData = [[tweet.user.screen_name.encode('utf-8'), tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')] for tweet in tweets]

# Create pandas dataframe
# tweet_text = pd.DataFrame(data=tweetData, 
#                     columns=['user', 'content', 'location'])

# tweet_text.to_csv('test.csv') 

