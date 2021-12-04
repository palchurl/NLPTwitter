#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import re, string
import numpy as np
import emoji
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize, sent_tokenize
import preprocessor as p
nltk.download('wordnet')
nltk.download('stopwords')

# Enter which list of tweets to read here:
filename = 'example.txt'

#importing list of tweets and encoding to utf-8
tweets = []
my_file = open(filename, "r")
tweets = my_file.readlines()

#tweets list is a list of strings
#tweets = [['Johnathan Pierce','Bright spot from the Panthers\xe2\x80\x99 27-21 loss yesterday? Christian McCaffrey became the fastest player in NFL history to hit 3,000 rushing yards and 3,000 receiving yards. \n\n@fox46\n\nFull #GoodDayCharlotte segment -&gt; https://t.co/2ti9VyJSiH https://t.co/iJpuqox99C',"@EASPORTS_MUT @RobGronkowski @JimmySmithJags @JasonTaylor IF JUSTIN JEFFERSON + DALVIN COOK DON'T GET A CARD SOON... I'll cry"],["Aaron Rodgers",'@new_dash_snow @rainIoss Derrick Henry is the bird the Titans are the person','@JayRBP I\xe2\x80\x99ll never understand Sean Payton using him running when he has Alvin Kamara','\xf0\x9f\x91\x89 $124.99 \xf0\x9f\x91\x88\nNFL PRO LINE Mens Ezekiel Elliott Navy Dallas Cowboys Big Tall Player @topfanscorner \n #PRO #LINE #Mens #Ezekiel #Elliott #Navy #Dallas #NFL #Football #NFLfans \n\nHurry up to get it for the best price!\nhttps://t.co/jgqpxZOYaA', 'Python is 👍']]

stemmer = PorterStemmer()
stopWordsList = set(stopwords.words('english'))
removeStopWords = ["hasn't", "not", "nor", "couldn't", "haven't", "isn't","mightn't", "aren't", "no", "didn't", "needn't","hadn't","shouldn't", "wouldn't", "doesn't", "mustn't"]
stopWordsList.difference_update(removeStopWords)

#get counts, least common words, most common words
ctr = Counter()
mostCommonWords = set()
leastCommonWords = set()
for player in tweets:
    for i in player[1:]:
        for j in i.split(" "):
            ctr[j] += 1    
for (i,c) in ctr.most_common(10):       #change 10 to get n most frequent
    mostCommonWords.add(i.lower())
for (i,c) in ctr.most_common()[:-11:-1]: #change 11 to get n least frequent
    leastCommonWords.add(i.lower())
print("most: ", mostCommonWords)
print("least: ", leastCommonWords)

def emojiToText(tweet):
    return emoji.demojize(tweet, delimiters=("", ""))

def removeMostandLeastFrequentWords(tweet):
    ans = ""
    for i in tweet.split():
        if i not in mostCommonWords and i not in leastCommonWords:
            ans = ans + i + " " 
    return ans

def stemWords(tweet):
    ans = ""
    for i in tweet.split():
        ans = ans + stemmer.stem(i) + " "
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

def preprocess(tweets):
    #tweet processor cleaner
    ans = []
    ctr = 0
    for i in tweets:
        if (ctr == 0):
            ans.append(i)
            ctr += 1
        else:
            # convert emojis to text/words
            afterEmojis = emojiToText(i)  
            # delete urls and mentions (@)
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
            # stemming
            afterStemming = stemWords(afterFreq)  #****
            # apply lemmatizer
            afterLemmatizer = lemmatizeTweets(afterStemming)
            #remove trailing/leading spaces
            extraspaces = afterLemmatizer.strip()
            ans.append(extraspaces)
    return ans

def main():
    for playerTweets in tweets:
        print("___________________")
        res = preprocess(playerTweets)
        print(res)
        
    
main()
