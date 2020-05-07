from collections import Counter

votes =['john','johnny','jackie','johnny','john','jackie', 
    'jamie','jamie','john','johnny','jamie','johnny','john']

# to get count of votes for each user
vote_count = Counter(votes)

# get max votes
max_votes = max(vote_count.values())

# create a list of election winners
lst = [i for i in vote_count.keys() if vote_count==max_votes]

# if there is a tie, print lexographically smaller one

print(sorted(lst)[0])