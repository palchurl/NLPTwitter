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

# Enter which list of players to read here:
filename = 'week11.txt'

#importing list of players
my_file = open(filename, "r")
players_list = my_file.readlines()

#print(players_list)

# Define the variables of the search (amount of tweets to be fetched (per player), and start date of the search)
date_since = "2021-11-19"
numTweets = 100

tweetData = []

for player in players_list:
     search_words = player + " -filter:retweets"
     
     # API fetch request
     tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              tweet_mode="extended",
              since=date_since).items(numTweets)
     
     tweetData.append([player] + [tweet.full_text.encode('utf-8') for tweet in tweets])


# Create pandas dataframe
# tweet_text = pd.DataFrame(data=tweetData, 
#                    columns=['content','1','2','3','4'])

# tweet_text.to_csv('draftpicks_corpus.csv') 

# Output to text file
textfile = open("alltweets_output.txt", "w")
for tweet in tweetData:
    textfile.write(str(tweet) + '\n' + '\n')
textfile.close()

