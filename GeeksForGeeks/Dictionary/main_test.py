from collections import Counter


votes =['john','johnny','jackie','johnny','john','jackie', 
    'jamie','jamie','john','johnny','jamie','johnny','john']

# count the votes for each person and store it in the dictionary
vote_count = Counter(votes)
print(type(vote_count))