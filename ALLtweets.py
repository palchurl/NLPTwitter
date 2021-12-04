import os
import tweepy as tw

# API keys
consumer_key= 'xJOSOBQIFQQZOKMAzZGf8RJvP'
consumer_secret= 'lkGh7uy3XeGKwuGWeXfjg5ud1wEb8VYFzcZTjjvH0XmNKsTNri'
access_token= '1420131687107813380-EUigVAo0abFTQUl62g0SZBeZAi7rFL'
access_token_secret= 'gQjlYJh2eDPN4kN5nnw59MP3axldx6P7wZ6YDhkFwwkbJ'

# Tweepy Authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Enter which list of players to read here:
filename = 'week12.txt'

#importing list of players
my_file = open(filename, "r")
players_list = my_file.readlines()

#print(players_list)

# Define the variables of the search (amount of tweets to be fetched (per player), and start date of the search)
date_since = "2021-11-26"
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

# Output to text file
textfile = open("alltweets_output.txt", "w")
for tweet in tweetData:
    textfile.write(str(tweet) + '\n' + '\n')
textfile.close()

