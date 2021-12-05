#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tweepy as tw
import nltk
import re, string
import numpy as np
import emoji
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from collections import Counter
from nltk import word_tokenize, sent_tokenize 
import preprocessor as p
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


nltk.download('wordnet')
nltk.download('stopwords')

#global vars
stopWordsList = set(stopwords.words('english'))
removeStopWords = ["hasn't", "not", "nor", "couldn't", "haven't", "isn't","mightn't", "aren't", "no", "didn't", "needn't","hadn't","shouldn't", "wouldn't", "doesn't", "mustn't"]
stopWordsList.difference_update(removeStopWords)

# API keys
consumer_key= '*****************'
consumer_secret= '*****************'
access_token= '*****************'
access_token_secret= '*****************'

# Tweepy Authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Enter which list of players to read here:
filename = 'week12.txt'

#importing list of players
my_file = open(filename, "r")
players_list = my_file.readlines()

# Define the variables of the search (amount of tweets to be fetched (per player), and start date of the search)
date_since = "2021-11-26"
numTweets = 100

tweetData = []

for player in players_list:
     search_words = player + " -filter:retweets"
     
     # API fetch request
     tweets = tw.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              tweet_mode="extended",
              since=date_since).items(numTweets)
     
     tweetData.append([player] + [tweet.full_text for tweet in tweets])

#get counts, least common words, most common words
ctr = Counter()
mostCommonWords = set()
leastCommonWords = set()
for player in tweets:
    for i in player[1:]:
        for j in i.split(" "):
            ctr[j] += 1    
for (i,c) in ctr.most_common(10):       
    mostCommonWords.add(i.lower())
for (i,c) in ctr.most_common()[:-11:-1]: 
    leastCommonWords.add(i.lower())
# print("most: ", mostCommonWords)
# print("least: ", leastCommonWords)

def emojiToText(tweet):
    return emoji.demojize(tweet, delimiters=("", ""))

def removeMostandLeastFrequentWords(tweet):
    ans = ""
    for i in tweet.split():
        if i not in mostCommonWords and i not in leastCommonWords:
            ans = ans + i + " " 
    return ans

def lemmatizeTweets(tweet):
    #Lemmatizer
    wnl = nltk.stem.WordNetLemmatizer()
    tt = TweetTokenizer()
    ans = ""
    for t in tt.tokenize(tweet):
        ans = ans + wnl.lemmatize(t) + " "
    return ans

def removeStopWords(tweet):
    ans = ""
    tweetWords = tweet.split(" ")
    for i in tweetWords:
        if i not in stopWordsList:
            ans = ans + i + " "
    return ans

names = []
def preprocess(tweets):
    ans = []
    ctr = 0
    name = ""
    for i in tweets:
        if (ctr == 0):
            names.append(i)
            # print(i)
            ctr += 1
        else:
            # convert emojis to text/words
            afterEmojis = emojiToText(i)  
            # delete urls and mentions (@)
            #print(i)
            cleaned = p.clean(afterEmojis)
            # remove digits 
            removedDigits = re.sub(r'[0-9]', '', cleaned)
            # remove punctuation
            removedPunct = re.sub(r'[^\w\s]', '', removedDigits)
            # make all the text lowercase
            lowercase = removedPunct.lower()     
            # remove extra spaces 
            extraspaces = re.sub(r' +', ' ', lowercase)
            # apply remove stop words
            afterStopWords = removeStopWords(extraspaces)
            # remove most and least frequent words
            afterFreq = removeMostandLeastFrequentWords(afterStopWords)
            # apply lemmatizer
            afterLemmatizer = lemmatizeTweets(afterFreq)
            #remove trailing/leading spaces
            extraspaces = afterLemmatizer.strip()
            ans.append(extraspaces)
    return [ans, names]


def sentimentAnalysisWithVader(processedTweets):
    sentimentScores = {}
    counter = pos = neg = neu =ctr= 0
    sentAnalyser = SentimentIntensityAnalyzer()
    playerTweetCounter = numTweets
    eachPlayersTweetScores = []
    for playerTweets in processedTweets:
        sent = sentAnalyser.polarity_scores(playerTweets)
        if (sent['compound'] >= 0.05):
            pos += 1
        elif (sent['compound'] <= - 0.05):
            neg += 1
        else:
            neu += 1
        ctr += 1
        playerTweetCounter = playerTweetCounter - 1
        eachPlayersTweetScores.append([sent['pos'], sent['neg'], sent['neu']])
        if(playerTweetCounter == 0):
            sentimentScores[names[counter]] = [(pos/ctr)*100, (neg/ctr)*100 , (neu/ctr)*100]
            counter += 1
            #reset all needed vars
            pos = neg = neu = 0
            playerTweetCounter = numTweets
            ctr = 0
            
    return [sentimentScores, eachPlayersTweetScores]

def graphSentimentScores(sent):
    x = []
    y = []
    z = []
    for i in sent:
        x.append(sent[i][0])
        y.append(sent[i][1])
        z.append(sent[i][2])

    fig = plt.figure(figsize = (10, 10))
    ax = plt.axes(projection ="3d")
    ax.scatter3D(x, y, z, color = "blue")
    ax.set_xlabel('Percentage Positive %', fontweight ='bold')
    ax.set_ylabel('Percentage Negative %', fontweight ='bold')
    ax.set_zlabel('Percentage Neutral %', fontweight ='bold')
    plt.title("Sentiment Plot", fontweight ='bold')
    plt.show()


def graphEachPlayersSentimentScores(sent):
    x = []
    y = []
    z = []
    playerCtr = 0
    ctr = numTweets
    for i in sent:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
        ctr = ctr-1
        if ctr == 0:
            fig = plt.figure(figsize = (10, 10))
            ax = plt.axes(projection ="3d")
            ax.scatter3D(x, y, z, color = "blue")
            ax.set_xlabel('Positive', fontweight ='bold')
            ax.set_ylabel('Negative', fontweight ='bold')
            ax.set_zlabel('Neutral', fontweight ='bold')
            plt.title(names[playerCtr], fontweight ='bold')
            plt.show()
            playerCtr = playerCtr + 1
            x = y = z = []
            ctr = numTweets

def main():
    processedTweets = []
    names = []
    for playerTweets in tweetData:
        res = preprocess(playerTweets)
        names = res[1]
        for i in res[0]:
            processedTweets.append([i])
    res = sentimentAnalysisWithVader(processedTweets)
    graphSentimentScores(res[0])
    # graphEachPlayersSentimentScores(res[1])

main()
