#Modules
import os
import csv
import itertools

#csv path for files:
input_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis","pollresults.txt")

#function to perform analysis:
def count_votes(input_file):
    #Variables definition:
    total_votes = 0
    candidate_names = []
    votes_per_candidate = {}
    per_candidate = []
    winner = ""
    votes = 0

    #count votes: each row in csvfile is a vote 
    for row in csvreader:
        #count total votes
        total_votes += 1
        #determine candidates names
        #if it is not in the list, the name is the a new key to add in the dictionary
        if row[2] not in candidate_names:
            candidate_names.append(str(row[2]))
            votes_per_candidate[row[2]] = 0
        #if it is in the list, the name is the key to add to the dictionary
        votes_per_candidate[row[2]] += 1

    #List comprehension of candidates with vote percentage and total votes:
    per_candidate = [f"{name}: {round(((votes_per_candidate[name]/total_votes)*100),3)}% ({votes_per_candidate[name]})" for name in candidate_names]

    #To find the winner, check who had more votes
    winnerindex = 0
    for name in candidate_names:    
        if votes_per_candidate[name] > winnerindex:
            winnerindex = votes_per_candidate[name]
            winner = name

    #save results in a list of strings
    results = ["Election Results",
               "-----------------------------",
               f"Total Votes: {total_votes}",
               "-----------------------------",
               *per_candidate,
               "-----------------------------",
               f"Winner: {winner}",
               "-----------------------------",]
    
    return results


#function to print and save:
def print_and_save(output_file):
    with open(output_file, "w") as text:

        for line in results:
            text.write(f"{line}\n")
            print(f"{line}\n")

#Open and read csv file:
with open(input_file) as csvfile:

    #initialize csv reader
    csvreader = csv.reader(csvfile, delimiter = ",")

    #save and skip header
    header = next(csvreader)

    #perform analysis:
    results = count_votes(input_file)

    #print and export a txtfile:
    print_and_save(output_file)