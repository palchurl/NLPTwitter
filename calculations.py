import matplotlib.pyplot as plt
import numpy as np
counter = 1
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
        y.extend([y[0]/y[1],y[0]-y[1],y[0]+y[1]])
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
    graph_calculations(players,"pos_neg_neu")
    graph_calculations(players,"div_sub_add")

    return positive_sort,negative_sort,neutral_sort,pos_div_neg_sort,pos_sub_neg_sort,pos_add_neg_sort
def graph_calculations(lis,name):
    global counter
    plt.rcdefaults()
    
    if type(lis) == dict:
        fig, ax = plt.subplots(figsize=(8, 6))
        people = [i for i,j in lis.items()]
        y_pos = np.arange(len(people))

        if name == "pos_neg_neu":
            performance = [j[0] for i,j in lis.items()]
            performance_two = [j[1] for i,j in lis.items()]
            performance_three = [j[2] for i,j in lis.items()]
            ax.barh(y_pos, performance,height=0.25,label="POS")
            ax.barh(y_pos+0.25, performance_two,height=0.25,label="NEG")
            ax.barh(y_pos+0.5, performance_three,height=0.25,label="NEU")
            ax.legend()
            counter += 1
        else:
            performance = [j[3] for i,j in lis.items()]
            performance_two = [j[4] for i,j in lis.items()]
            performance_three = [j[5] for i,j in lis.items()]
            ax.barh(y_pos, performance,height=0.25,label="POS_DIV_NEG")
            ax.barh(y_pos+0.25, performance_two,height=0.25,label="POS_SUB_NEG")
            ax.barh(y_pos+0.5, performance_three,height=0.25,label="POS_ADD_NEG")
            ax.legend()
            counter += 1
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.set_ylabel('Athletes')
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Scores')
        ax.set_title('Tweets')
        fig.tight_layout()
        plt.show()         #uncomment to view fig
        fig.savefig("fig_"+str(counter)+"_"+name)  #uncomment to save fig
    else:
        fig, ax = plt.subplots(figsize=(8, 6))
        people = [i for i,j in lis]
        y_pos = np.arange(len(people))
        performance = [j for i,j in lis]
        ax.barh(y_pos, performance,height=0.25)
        counter+=1
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.set_ylabel('Athletes')
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Scores')
        ax.set_title('Tweets')
        fig.tight_layout()
        plt.show()         #uncomment to view fig
players11 = {'Jonathan Taylor\n': [44.0, 8.0, 48.0], 'Austin Ekeler\n': [36.0, 15.0, 49.0], 'Justin Herbert\n': [37.0, 18.0, 45.0], 'Aaron Rodgers\n': [34.0, 30.0, 36.0], 'Jalen Hurts\n': [18.0, 76.0, 6.0], 'Justin Jefferson\n': [27.0, 8.0, 65.0], 'Cam Newton\n': [38.0, 24.0, 38.0], 'Chris Jones\n': [42.0, 24.0, 34.0], 'Kirk Cousins\n': [46.0, 17.0, 37.0], 'Joe Mixon\n': [38.0, 16.0, 46.0], 'Trevor Siemian\n': [41.0, 36.0, 23.0], 'Davante Adams\n': [47.0, 20.0, 33.0], 'Taylor Heinicke\n': [44.0, 17.0, 39.0], 'Colt McCoy\n': [52.0, 28.000000000000004, 20.0], 'Ben Roethlisberger\n': [31.0, 26.0, 43.0], 'Elijah Moore\n': [46.0, 14.000000000000002, 40.0], 'Zach Ertz': [46.0, 18.0, 36.0]}
players12 = {'Leonard Fournette\n': [49.0, 33.0, 18.0], 'Joe Mixon\n': [34.0, 25.0, 41.0], 'Josh Allen\n': [44.0, 35.0, 21.0], 'Aaron Rodgers\n': [34.0, 23.0, 43.0], 'Cordarrelle Patterson\n': [39.0, 19.0, 42.0], 'Dak Prescott\n': [47.0, 16.0, 37.0], 'Elijah Mitchell\n': [22.0, 52.0, 26.0], 'Matthew Stafford\n': [43.0, 14.000000000000002, 43.0], 'Mac Jones\n': [56.00000000000001, 11.0, 33.0], 'Derek Carr\n': [55.00000000000001, 20.0, 25.0], 'Carson Wentz\n': [25.0, 19.0, 56.00000000000001], 'Daniel Carlson\n': [39.0, 21.0, 40.0], 'Nick Folk \n': [31.0, 22.0, 47.0], 'Deebo Samuel \n': [34.0, 23.0, 43.0], 'Justin Herbert\n': [41.0, 21.0, 38.0], 'Jaylen Waddle\n': [38.0, 15.0, 47.0]}
players13 = {'Kyler Murray\n': [64.0, 8.0, 28.000000000000004], 'George Kittle\n': [32.0, 32.0, 36.0], 'Tom Brady\n': [40.0, 34.0, 26.0], 'Justin Herbert\n': [30.0, 22.0, 48.0], 'Justin Jefferson\n': [24.0, 30.0, 46.0], 'Jonathan Taylor\n': [26.0, 34.0, 40.0], 'Matthew Stafford\n': [28.000000000000004, 24.0, 48.0], 'Javonte Williams\n': [36.0, 18.0, 46.0], 'Dallas Goedert\n': [48.0, 18.0, 34.0], 'Diontae Johnson\n': [40.0, 24.0, 36.0], 'Zach Wilson\n': [44.0, 24.0, 32.0], 'Taysom Hill\n': [30.0, 24.0, 46.0], 'Kirk Cousins\n': [46.0, 20.0, 34.0], 'David Montgomery\n': [48.0, 12.0, 40.0], 'Jared Goff\n': [18.0, 56.00000000000001, 26.0], 'Tee Higgins\n': [28.000000000000004, 30.0, 42.0], 'Ben Roethlisberger\n': [34.0, 16.0, 50.0], 'Cooper Kupp\n': [38.0, 24.0, 38.0], 'Sony Michel\n': [40.0, 22.0, 38.0], 'Gardner Minshew': [38.0, 36.0, 26.0]}
players14 = {'Josh Allen\n': [50.0, 24.0, 26.0], 'Dalvin Cook\n': [44.0, 22.0, 34.0], 'Tom Brady\n': [48.0, 20.0, 32.0], 'Aaron Rodgers\n': [56.00000000000001, 26.0, 18.0], 'Taysom Hill\n': [54.0, 18.0, 28.000000000000004], 'Rashaad Penny\n': [57.99999999999999, 10.0, 32.0], 'Justin Herbert\n': [50.0, 18.0, 32.0], 'Ben Roethlisberger\n': [38.0, 34.0, 28.000000000000004], 'James Conner\n': [44.0, 26.0, 30.0], 'Davante Adams\n': [57.99999999999999, 10.0, 32.0], 'Matthew Stafford\n': [56.00000000000001, 18.0, 26.0], 'Melvin Gordon\n': [62.0, 16.0, 22.0], 'Najee Harris\n': [38.0, 34.0, 28.000000000000004], 'Joe Burrow\n': [54.0, 18.0, 28.000000000000004], 'Tyler Lockett\n': [48.0, 20.0, 32.0], 'Russell Wilson\n': [40.0, 26.0, 34.0], 'George Kittle\n': [50.0, 12.0, 38.0], 'Alvin Kamara\n': [62.0, 14.000000000000002, 24.0], 'Patrick Mahomes\n': [46.0, 14.000000000000002, 40.0], "Ja'Marr Chase\n": [46.0, 20.0, 34.0], 'Javonte Williams\n': [40.0, 12.0, 48.0], 'Jimmy Garoppolo\n': [52.0, 18.0, 30.0], 'Leonard Fournette\n': [60.0, 24.0, 16.0], 'Aaron Jones\n': [62.0, 16.0, 22.0], 'Justin Fields\n': [38.0, 24.0, 38.0], 'Mike Glennon\n': [48.0, 30.0, 22.0], 'Cooper Kupp\n': [46.0, 18.0, 36.0], 'Davis Mills\n': [26.0, 22.0, 52.0], 'Mark Andrews\n': [42.0, 16.0, 42.0], 'Kyler Murray\n': [48.0, 32.0, 20.0], 'Ryan Tannehill\n': [52.0, 24.0, 24.0], 'Clyde Edwards-Helaire\n': [26.0, 20.0, 54.0], 'Hunter Renfrow\n': [28.000000000000004, 18.0, 54.0], 'Saquon Barkley\n': [70.0, 16.0, 14.000000000000002], 'Tyler Huntley\n': [62.0, 24.0, 14.000000000000002], 'Teddy Bridgewater\n': [56.00000000000001, 24.0, 20.0], 'Mike Evans\n': [44.0, 24.0, 32.0], 'Baker Mayfield\n': [44.0, 36.0, 20.0], 'Allen Lazard\n': [56.00000000000001, 18.0, 26.0], 'Derrick Gore': [40.0, 14.000000000000002, 46.0]}
player_dic(players11)
player_dic(players12)
player_dic(players13)
player_dic(players14)
