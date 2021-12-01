from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

processedTweets = [['Johnathan Pierce', 'panther yesterday christian mccaffrey became fastest player nfl history hit rushing yard receiving yard segment gt', 'justin jefferson dalvin cook dont card soon ill cry'], ['Aaron Rodgers', 'derrick henry bird titan person', 'ill never understand sean payton using running alvin kamara', 'nfl pro line men ezekiel elliott navy dallas cowboy big tall player hurry price', 'thumbs_up']]

def sentimentAnalysisWithVader(processedTweets):
    sentimentScores = {}
    sentAnalyser = SentimentIntensityAnalyzer()
    for playerTweets in processedTweets:
        ctr = -1
        pos = neg = neu = 0
        player = ""
        for i in playerTweets:
            if ctr == -1:
                player = i
                ctr += 1
            else:
                sent = sentAnalyser.polarity_scores(i)
                if (sent['compound'] >= 0.05):
                    pos += 1
                elif (sent['compound'] <= - 0.05):
                    neg += 1
                else:
                    neu += 1
                ctr += 1
        sentimentScores[player] = [(pos/ctr)*100, (neg/ctr)*100, (neu/ctr)*100]
    return sentimentScores

def graphSentimentScores(sent):
    x = []
    y = []
    z = []
    for i in sent:
        print(sent[i])
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

def main():            
    res = sentimentAnalysisWithVader(processedTweets)
    graphSentimentScores(res)

main()
