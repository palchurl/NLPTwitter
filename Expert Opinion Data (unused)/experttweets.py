import os
import tweepy as tw

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
filename = 'week11_fullnames.txt'

#importing list of players
my_file = open(filename, "r")
players_list = my_file.readlines()
#players_list = [x[:-1] for x in players_list]
#print(players_list)

#importing list of experts
my_file = open("expertslist.txt", "r")
experts_list = my_file.readlines()
#experts_list = [x[:-1] for x in experts_list]
#print(experts_list)

# Choose how many tweets to search (per account)
numTweets = 1000

tweetData = []

for expert in experts_list:
    try:
        # API fetch request
        tweets = api.user_timeline(screen_name = expert, count = numTweets, lang = "en", tweet_mode = "extended")
        # Search for player names within collected tweets
        for player in players_list:
            for tweet in tweets:
                if player in tweet.full_text:
                    tweetData.append([player + ' ' + tweet.full_text.encode('utf-8')])
    except: 
        print('User not found: ' + expert)


# Output to text file
textfile = open("experttweets_output.txt", "w")
for tweet in tweetData:
    textfile.write(str(tweet) + '\n' + '\n')
textfile.close()

