import matplotlib.pyplot as plt
#import numpy as np
def player_dic(players):
    pos=[]
    neg=[]
    neu=[]
    pos_div_neg=[]
    pos_sub_neg=[]
    pos_add_neg=[]
    for x,y in players.items():
        pos.append([x,y[0]])
        neg.append([x,y[1]])
        neu.append([x,y[2]])
        pos_div_neg.append([x,y[0]/y[1]])
        pos_sub_neg.append([x,y[0]-y[1]])
        pos_add_neg.append([x,y[0]+y[1]])
    positive_sort = sorted(pos, key=lambda x: x[1])
    negative_sort = sorted(neg, key=lambda x: x[1])
    neutral_sort = sorted(neu, key=lambda x: x[1])
    pos_div_neg_sort = sorted(pos_div_neg, key=lambda x: x[1])
    pos_sub_neg_sort = sorted(pos_sub_neg, key=lambda x: x[1])
    pos_add_neg_sort = sorted(pos_add_neg, key=lambda x: x[1])

    graph_calculations(positive_sort,"positive_sort")
    graph_calculations(negative_sort,"negative_sort")
    graph_calculations(neutral_sort,"neutral_sort")
    graph_calculations(pos_div_neg_sort,"pos_div_neg_sort")
    graph_calculations(pos_sub_neg_sort,"pos_sub_neg_sort")
    graph_calculations(pos_add_neg_sort,"pos_add_neg_sort")

    return positive_sort,negative_sort,neutral_sort,pos_div_neg_sort,pos_sub_neg_sort,pos_add_neg_sort
def graph_calculations(lis,name):
    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=(8, 6))

    people = [i for i,j in lis]
    y_pos = np.arange(len(people))
    performance = [j for i,j in lis]

    ax.barh(y_pos, performance,height=0.25)
    #ax.barh(y_pos+0.25, pperformance, height=0.25)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.set_ylabel('Athletes')
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Scores')
    ax.set_title('Tweets')
    fig.tight_layout()
    plt.show()         #uncomment to view fig
    # fig.savefig(name)  #uncomment to save fig
players = {'Leonard Fournette\n': [49.0, 33.0, 18.0], 'Joe Mixon\n': [34.0, 25.0, 41.0], 'Josh Allen\n': [44.0, 35.0, 21.0], 'Aaron Rodgers\n': [34.0, 23.0, 43.0], 'Cordarrelle Patterson\n': [39.0, 19.0, 42.0], 'Dak Prescott\n': [47.0, 16.0, 37.0], 'Elijah Mitchell\n': [22.0, 52.0, 26.0], 'Matthew Stafford\n': [43.0, 14.000000000000002, 43.0], 'Mac Jones\n': [56.00000000000001, 11.0, 33.0], 'Shaquil Barrett\n': [36.0, 23.0, 41.0], 'Derek Carr\n': [55.00000000000001, 20.0, 25.0], 'Carson Wentz\n': [25.0, 19.0, 56.00000000000001], 'Jaelan Phillips \n': [37.0, 25.0, 38.0], 'Daniel Carlson\n': [39.0, 21.0, 40.0], 'Nick Folk \n': [31.0, 22.0, 47.0], 'Deebo Samuel \n': [34.0, 23.0, 43.0], 'Justin Herbert\n': [41.0, 21.0, 38.0], 'Jaylen Waddle\n': [38.0, 15.0, 47.0]}
player_dic(players)