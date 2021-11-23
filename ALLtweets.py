import os
import tweepy as tw
import pandas as pd

# API keys
consumer_key= 'xJOSOBQIFQQZOKMAzZGf8RJvP'
consumer_secret= 'lkGh7uy3XeGKwuGWeXfjg5ud1wEb8VYFzcZTjjvH0XmNKsTNri'
access_token= '1420131687107813380-EUigVAo0abFTQUl62g0SZBeZAi7rFL'
access_token_secret= 'gQjlYJh2eDPN4kN5nnw59MP3axldx6P7wZ6YDhkFwwkbJ'

# Tweepy Authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#importing list of players
players_dict = {}
my_file = open("draftpicks.txt", "r")
players_list = my_file.readlines()

#print(players_list)

# Define the variables of the search (player name, amount of tweets to be fetched, and start date of the search)

date_since = "2021-11-14"
numTweets = 1
tweetData = []

for player in players_list:
     search_words = player + " -filter:retweets"
     
     # API fetch request
     tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              tweet_mode="extended",
              since=date_since).items(numTweets)
     # tweetInfo = [[tweet.user.screen_name.encode('utf-8'), tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')] for tweet in tweets]
     
     #tweetInfo = [tweet.full_text.encode('utf-8') for tweet in tweets]
     tweetData.append([tweet.full_text.encode('utf-8') for tweet in tweets])

     #tweetData.append(tweetInfo)

# Collect more info about tweet
# tweetData = [[tweet.user.screen_name.encode('utf-8'), tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')] for tweet in tweets]

# Create pandas dataframe
# tweet_text = pd.DataFrame(data=tweetData, 
#                    columns=['content','1','2','3','4'])

# tweet_text.to_csv('draftpicks_corpus.csv') 

# Output to text file
textfile = open("example.txt", "w")
for tweet in tweetData:
    textfile.write(str(tweet) + '\n' + '\n')
textfile.close()

# Print tweets
# for tweet in tweetData:
#       print(tweet)

