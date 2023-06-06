# import the csv file
import csv


# locate and open the csv file in read form
with open("resources/election_data.csv", "r") as f:

    reader = csv.reader(f)
    election_data = list(reader)

# assign a title
title = "Election Results"
print(title)
print("----------------------------------------")

# calculate the total number of votes cast
total_votes = len(election_data)
print("The total number of votes cast:", total_votes)
print("----------------------------------------")

# list the candidates that recieved votes

#list_candidates = []
