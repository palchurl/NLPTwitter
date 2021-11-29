from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

processedTweets = [['Johnathan Pierce', 'panther yesterday christian mccaffrey became fastest player nfl history hit rushing yard receiving yard segment gt', 'justin jefferson dalvin cook dont card soon ill cry'], ['Aaron Rodgers', 'derrick henry bird titan person', 'ill never understand sean payton using running alvin kamara', 'nfl pro line men ezekiel elliott navy dallas cowboy big tall player hurry price', 'thumbs_up']]
def sentimentAnalysisWithVader(processedTweets):
    sid_obj = SentimentIntensityAnalyzer()
    for playerTweets in processedTweets:
        ctr = 0
        for i in playerTweets:
            if ctr == 0:
                print("Player: ",i)
                ctr += 1
            else:
                print("Tweet: ", i)
                sentiment_dict = sid_obj.polarity_scores(i)
                print("Overall sentiment dictionary is : ", sentiment_dict)
                print("Pos: ",sentiment_dict['pos']*100, "%")
                print("Neu: ", sentiment_dict['neu']*100, "%")
                print("Neg: ", sentiment_dict['neg']*100, "%")
                
                if (sentiment_dict['compound'] >= 0.05):
                    print("Positive")
                elif (sentiment_dict['compound'] <= - 0.05):
                    print("Negative")
                else:
                    print("Neutral")
                print("")
                
sentimentAnalysisWithVader(processedTweets)
