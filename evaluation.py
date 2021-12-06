from scipy.stats import kendalltau

###### Evaluation Process:
# Step 1: In sentiment_output, sort players by some measure of positive sentiment
# Step 2: In week11.txt, assign each player a number 1-20
# Step 3: In sentiment_output, assign each player numbers according to numbers from week11.txt, new players not on week11.txt will be given numbers >20
# Step 4: Create two lists with those numbers, one list will represent the actual rankings 1-20 from week11.txt, the other will represent the players ranked by sentiment_output
# Step 5: Calculate kendalltau between both lists to determine the correlation

# Interpretation of Kendall Tau
# Notice that the maximum and minimum value that 𝛕 can take is +1 and -1 respectively. +1 denotes perfect agreement and -1 denotes complete disagreement. 
# A value of 0 means that there is no correlation between the rankings. 

# Taking values from the above example in Lists
rankings_actual = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
rankings_sentiment = [1, 3, 11, 2, 7, 4, 5, 9, 10, 6, 12, 13, 14, 21, 16, 17, 8, 19, 20, 22]
  
# Calculating Kendall Rank correlation
corr, _ = kendalltau(rankings_actual, rankings_sentiment)
print('Kendall Rank correlation: %.5f' % corr)