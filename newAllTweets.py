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
# import contractions 
import preprocessor as p

nltk.download('wordnet')
nltk.download('stopwords')

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
filename = 'week12.txt'

#importing list of players
my_file = open(filename, "r")
players_list = my_file.readlines()

#print(players_list)

# Define the variables of the search (amount of tweets to be fetched (per player), and start date of the search)
date_since = "2021-11-26"
numTweets = 100

tweets = []

for player in players_list:
     search_words = player + " -filter:retweets"
     
     # API fetch request
     tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              tweet_mode="extended",
              since=date_since).items(numTweets)
     
     tweets.append([player] + [tweet.full_text.encode('utf-8') for tweet in tweets])

# Output to text file
# textfile = open("alltweets_output.txt", "w")
# for tweet in tweets:
#     textfile.write(str(tweet) + '\n' + '\n')
# textfile.close()


#tweets list is a list of strings
#tweets = [['Johnathan Pierce','Bright spot from the Panthers\xe2\x80\x99 27-21 loss yesterday? Christian McCaffrey became the fastest player in NFL history to hit 3,000 rushing yards and 3,000 receiving yards. \n\n@fox46\n\nFull #GoodDayCharlotte segment -&gt; https://t.co/2ti9VyJSiH https://t.co/iJpuqox99C',"@EASPORTS_MUT @RobGronkowski @JimmySmithJags @JasonTaylor IF JUSTIN JEFFERSON + DALVIN COOK DON'T GET A CARD SOON... I'll cry"],["Aaron Rodgers",'@new_dash_snow @rainIoss Derrick Henry is the bird the Titans are the person','@JayRBP I\xe2\x80\x99ll never understand Sean Payton using him running when he has Alvin Kamara','\xf0\x9f\x91\x89 $124.99 \xf0\x9f\x91\x88\nNFL PRO LINE Mens Ezekiel Elliott Navy Dallas Cowboys Big Tall Player @topfanscorner \n #PRO #LINE #Mens #Ezekiel #Elliott #Navy #Dallas #NFL #Football #NFLfans \n\nHurry up to get it for the best price!\nhttps://t.co/jgqpxZOYaA', 'Python is 👍']]
#tweetsCopy = [['Jonathan Taylor\n', 'One day left on this Jonathan Taylor RPA /99 from Panini One #rookie #colts #panini #nfl\nhttps://t.co/SoDQAx5cXm', '#Texans roster moves: OL Lane Taylor signed from the practice squad. DE Jordan Jenkins placed on IR. DB Jonathan Owens elevated from practice squad (standard).', '@DjangoEra im playing all madden competitive \xf0\x9f\x98\xad i traded dalvin cook for Jonathan Taylor and Pittman, and already had Jefferson since its the vikings', '@FantasyPros I got Jonathan Taylor for Keenan Allen straight up between weeks 3 and 4', '\xe2\x81\x83Highest Scoring Keeper:\nJonathan Taylor (51.9) We Off The Griddy\n\xe2\x81\x83The Bill Belichick Award\nWe Off The Griddy (127.3)\n\xe2\x81\x83The Hue Jackson Award\nCatalina Wine Mixon (79.94)\n\xe2\x81\x83The Boom Award\nJonathan Taylor (51.9) We Off The Griddy', "On the latest episode of The X Report, we discuss Jonathan Taylor's MVP chances, discuss the altercation between LeBron James and Isaiah Stewart, and recap #SurvivorSeries. @Bigenopoppa901 #TheXReportTakeOver\n https://t.co/Uvg1ICckyi", 'going away easily either. But Akers was drafted to be the bellcow in this offense and his talent will be too much to hold him back for long. Let\xe2\x80\x99s look back to the end of his rookie season. Akers came on strong late in the season, much like what we saw from Jonathan Taylor\xe2\x80\xa6', 'Jonathan Taylor esk. Dudes gonna be a beast in the NFL. #NFL #NFLDraft #NFLTwitter #MichiganWolverines https://t.co/FdUjeIWdL3', 'Jonathan Taylor obviously https://t.co/sLRX3uOJSB', 'Jonathan Larson\xe2\x80\x99s 30/90 and Taylor Swift\xe2\x80\x99s Nothing New have the same vibe\n#TickTickBoom #RedTaylorsVersion', '@Curious_Colt As long as Jonathan Taylor touches the ball 25 times colts will win 30-20 Colts', 'going away easily either. But Akers was drafted to be the bellcow in this offense and his talent will be too much to hold him back for long. Let\xe2\x80\x99s look back to the end of his rookie season. Akers came on strong late in the season, much like what we saw from Jonathan Taylor\xe2\x80\xa6', 'Haskins is the new Jonathan Taylor', 'GMFB | Kyle Brandt claims Colts RB Jonathan Taylor will shine brightest against Bucs in NFL Week\xc2\xa012 https://t.co/zJ0wGHsIcL', '@jakebeleafs @BudsAllDayCast @sforys92 this will look great on jonathan taylor in a couple months', "@InselmannTyler I can't get past Robinson. I know he was a Tuscaloosa kid. But recruiting him baffled me. That 2017 high-school class was legendary. \nNajee Harris, Cam Akers, DeAndre Swift, JK Dobbins, Trey Sermon, Jonathan Taylor, Clyde Edwards Elaire, Travis Entienne, AJ Dillon...wtf?", '@CFBHeather Jonathan Taylor, too.', 'Jonathan Taylor https://t.co/0hhvBVUXWA', '"JWill says that Jonathan Taylor winning the MVP is an overreaction | KJM" #SportsVideo #ESPN #SkySports #FoxSports #NBCSN #Sportsnet #NFLNetwork: https://t.co/tBjDzdVuOV', '@FantasyPros Traded for Cook/Mattison to pair with Jonathan Taylor. Have David Montgomery and Kareem Hunt for my flex. Also J. Williams and. D. Harris to break glass in case of emergency. I feel good about it. https://t.co/bQi6grwuiY', '@FantasyPros I traded Dak &amp; Kelce for Hurts, Jonathan Taylor and a 3rd \xf0\x9f\x94\xa5 \xf0\x9f\x94\xa5 \xf0\x9f\x94\xa5', '@FantasyPros I got Jonathan Taylor, Diontae Johnson, and Jalen Hurts for Dak, Ridley, and Darrell Henderson early in the season.', 'The Best player from every AFC South Team. What is your opinion on this? Comment down Below.\n\nColts - Jonathan Taylor \nTexans - Laremy Tunsil \nJaguars - Josh Allen \nTitans - Derrick Henry', '@Eagles76ersTalk @Colts_Law Them ask him What\xe2\x80\x99s the colts record when Jonathan Taylor runs for 100+?', 'What2Watch4 #TBvsIND\n\n1. Jonathan Taylor vs #4 run DVOA D (just 1 RB 100+ yd)\n1a.\xf0\x9f\x92\xa4route/db last 3: 48%, 50%, 71%\n2. Michael Pittman FP/g w/ Hilton 13.5, w/o: 16\n2a. \xe2\x89\xa45 tgt in 3/4 wk w/ TY\n3. Gronk vs IND D: #6 most FP, #2 most yd to TE\n4. Lenny Fournette\xe2\x9d\x84\xef\xb8\x8fvs IND lowest FP to RB https://t.co/x2X3lmFAI0', "Does anyone know a place that sells Nike Vapor Elite jerseys in Indy? I am looking to buy a Jonathan Taylor jersey. The guy on the phone for @Colts ProShop at Lucas Oil said they don't have them. No I don't want to buy one from KWeav. thanks guys!", "@HutzSR @NFLAllDay Dude is taking 5 weeks off from a minor ankle sprain. I'm his biggest fan, have him in many of my leagues, but there are a lot of players left out in the 30 second clip who are more deserving this year. Lamar Jackson, Jonathan Taylor, Cooper Kupp to name, etc, etc.", '@Dan_Salomone @Giants I don\xe2\x80\x99t think Jonathan Taylor agrees with you Dan', 'this dude watched Jonathan Taylor last week and said \xe2\x80\x9cim tryna be like that\xe2\x80\x9d then went and did the damn thing https://t.co/FJ2u66yiwo', "Very aware that B1G folks will compare Braelon Allen to Jonathan Taylor. Understood, but that's not who comes to mind on this end.....\n\n....this is a taller, lighter Ron Dayne in his prime. Watch out for this guy.\n\n#OnWisconsin #Badgers", "@Holy_Porks Jonathan Taylor has 26 fewer carries than Derrick Henry this season. He has 185 more rushing yards, 3 more rushing TDs, and 19 more rushing 1st downs.\n\nTaylor is averaging 5.8 yards/carry vs. Henry's 4.3. \nTaylor has gained a first down on 35.2% of his carries vs. Henry's 22.4%.", 'Anyone fading Jonathan Taylor in @FanDuel this week?\n\n#FantasyFootball #FanDuel #NFL', '@Colts_Law He can thank Jonathan Taylor for saving his football career', '@braydoncook3120 @DemonTimeJmo @AdamSchefter Jonathan Taylor RUNS the AFC', 'JONATHAN TAYLOR TD -200 \xf0\x9f\xa4\xae', 'In the past two weeks Jonathan Taylor and Hassan Haskins have carved my two favorite teams for 10 TDs combined. I am not alright \xf0\x9f\x98\x96\xf0\x9f\x98\xaa', 'Marshawn Lynch really gave Jonathan Taylor a little pep talk in the tunnel prior to his 5TD performance vs BUF in week 11 \xf0\x9f\x91\x80', '@H2_3125 Hassan Haskins pulls a Jonathan Taylor for the WIN!!!!!!!!!!', '@JoeyBFutureMVP in my franchise i got lamar, jonathan taylor, and justin jefferson to 95+ in like 2 years \xf0\x9f\x98\xad', '@josephLrendon @MiamiDolphins @Noah_Igbo9 @FloridaFUTP60 He\xe2\x80\x99s a useless bum. Not every fan likes every single player on their favorite team. Yes I\xe2\x80\x99d rather have Jonathan Taylor. What Dolphin fan wouldn\xe2\x80\x99t ?  Now go sit in the corner you moron', 'Texans sign guard Lane Taylor to active roster, place Jordan Jenkins on IR with torn PCL, elevated Jonathan Owens https://t.co/xii0RgmvoT', '@FantasyPros In Dynasty, after CMC went down in WK 3, I  traded Herbert, Lockett, M.Williams, M.Davis, a 2022 1st Rnd Pick, $50 Bid dollars for DeVante Adams and Jonathan Taylor\xe2\x80\xa6\xf0\x9f\x92\xaa\xf0\x9f\x8f\xbb\xf0\x9f\x98\x8e', 'Watching the media basically beg one of the QBs to win MVP weekly is sad. \n\nJonathan Taylor gets nothing but excuses, He\xe2\x80\x99s gotta have a 2K yard season and break every RB record set since Jim Brown was playing ?!?', 'Since Week 3, Jonathan Taylor has eclipsed 20 PPR points in all but one game (Week 7).\n\nMeanwhile, the young back has surpassed 30 PPR points on three other occasions, including his 53.4 point outburst vs the Bills.\n\nThere\xe2\x80\x99s no more consistent fantasy player at this time!\n\n#RTDB', '@PFF Damn. No Michael Pittman or Jonathan Taylor?', "@jeff_zill @MVP2494 @joeybrown77 @UMichFootball jonathan taylor has really good potential and he's displaying it this season\ncould be OPOY with derrick henry out", '@jeff_zill @MVP2494 @joeybrown77 @UMichFootball jonathan taylor was a beast in college', 'Sounds like Jonathan Taylor numbers? https://t.co/yNAHtLPing', 'Hope Jonathan Taylor drops 80 on Brady\xe2\x80\x99s head tomorrow', "Texans place Jordan Jenkins on IR with torn PCL, signed Lane Taylor to active roster, elevated Jonathan Owens. Didn't activate Justin Britt from IR designated for return, but could as soon as next week. Rookie Jimmy Morrissey to start third game in a row", 'We just saw a fine performance by Michigan RB Hassan Haskins. Now\xe2\x80\x99s the perfect time to check out a few RBs I think will make their fair share of big plays on Sundays. Here\xe2\x80\x99s my latest on @TheAthleticFS \xf0\x9f\x91\x87\xf0\x9f\x8f\xbf\n\nRunning backs to the future: https://t.co/YyckTUSCBw', '@FantasyPros I traded \nDalvin Cook &amp; D.K Metcalf \nFor Jonathan Taylor &amp; Terry McLaurin \nBiggest Win for me.', 'Last week we nailed HOU ML as a 10pt underdog, Anthony Firkser TD +420 and Jonathan Taylor going OFF.\n\nJoin me at 10am EST on @DimersCom IG live to go through the full Sunday slate!\n\nBring your coffee and your best plays to discuss.\n\n#GamblingTwitter https://t.co/6PQzOXMty0', 'Dude pulled a Jonathan Taylor. Yeesh \xf0\x9f\x98\xb6 https://t.co/9WvX8rBCl4', '@ChrisMc65732296 @Colts_Law @CPFelger55 Did he do it or did Jonathan Taylor do it? Cuz Wentz it\xe2\x80\x99s better then brisset  but that dosent make him luck. How much faith do you have in Wentz arm on a scale of 1-5? I want him to succeed but I\xe2\x80\x99m not gonna grown him the heir to 18 and 12 after 1 season.', '@PFF_College @PFF @UMichFootball Channeled his inner Jonathan Taylor', 'Bro said the Indianapolis Jonathan Taylor\xe2\x80\x99s\xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x98\xad\xf0\x9f\x98\xad https://t.co/mLTbsXViKW', 'Hassan Haskin just worked OSU like Jonathan Taylor in Week 11 against The Buffalo Bills', '@_BrandonWallace Does Jonathan Taylor have eligibility', '@BrettIsNotATree @NFL Yes, like Jonathan Taylor and Cooper Kupp. #1 in their position ranking because they\xe2\x80\x99ve been the most productive players at their position. Can\xe2\x80\x99t deny the greatness of those players. Allen\xe2\x80\x99s been the most productive QB', '@CHBillsJaysfan @emilymkaplan jonathan taylor owns your franchise']]
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

# def expandContractions(tweet):
#     contractions = Contractions(api_key="glove-twitter-100")
#     contractions.expand_texts([])  
#     expandedTweet = contractions.expand_texts(tweet, precise=False)
#     print(expandedTweet)
#     return expandedTweet

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
            # expand contractions
            # afterExpansion = expandContractions(afterEmojis)
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
            # apply lemmatizer
            afterLemmatizer = lemmatizeTweets(afterFreq)
            #remove trailing/leading spaces
            extraspaces = afterLemmatizer.strip()
            ans.append(extraspaces)
    return ans

for playerTweets in tweets:
   print("___________________")
   res = preprocess(playerTweets)
   print(res)
   for i in res:
       print(i)

    
