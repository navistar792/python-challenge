import os
import csv

# first, add variables to store the total votes, with a starting point of zero
tot_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
# added "other" as a data quality check to see if there were any votes for other candidates
other_votes = 0

# used to provide the winner in the output. For learning, I wanted to incorporate a list or two
candidates = ["Khan","Correy","Li","O'Tooley"]
cand_votes = []

# Path to collect data from the Resources folder
pypoll_csv = os.path.join("Resources", "election_data.csv")

# Use encoding for Windows
with open(pypoll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        # add votes to this variable as the code iterates through the data
        tot_votes = tot_votes + 1
        # count votes for each candidate
        if row[2] in candidates[0]:
            khan_votes = khan_votes + 1
        elif row[2] in candidates[1]:
            correy_votes = correy_votes + 1
        elif row[2] in candidates[2]:
            li_votes = li_votes +1
        elif row[2] in candidates[3]:
            otooley_votes = otooley_votes + 1
        else:
            # just in case there are blanks or write-ins. There aren't any, so I omitted this from the output
            other_votes = other_votes +1   

# append the total votes for each candidate to a list so that the winner can be provided to the output
cand_votes.append(khan_votes)
cand_votes.append(correy_votes)
cand_votes.append(li_votes)
cand_votes.append(otooley_votes)

# calculate percentages and assign to variables
khan_pct = round((khan_votes/tot_votes)*100,3)
correy_pct = round((correy_votes/tot_votes)*100,3)
li_pct = round((li_votes/tot_votes)*100,3)
otooley_pct = round((otooley_votes/tot_votes)*100,3)
# Find greatest value in the list  
max_value = max(cand_votes)
# and find the index for the greatest value to print the name of the winner
max_index = cand_votes.index(max_value)

# define a function to print the results
def print_results():
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes:  ({tot_votes})")        
    print("--------------------------")
    print(f"Khan: {khan_pct}% ({khan_votes})")
    print(f"Correy: {correy_pct}% ({correy_votes})")
    print(f"Li: {li_pct}% ({li_votes})")
    print(f"O'Tooley: {otooley_pct}% ({otooley_votes})")
    # next line not needed in output - ran to verify that all votes fell within the 4 candidates
    # print(f"Other: {round(other_votes/tot_votes*100,3)}% ({other_votes})")
    print("--------------------------")
    print(f"Winner: {candidates[max_index]}")
    print("--------------------------")

print_results()

# results output to a file
# Specify the file to write to
output_path = os.path.join("analysis", "pypoll.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Description', '%','Votes'])

    # Write the second row
    csvwriter.writerow(['Total Votes ','', tot_votes])

    # Write the third row
    csvwriter.writerow([candidates[0],khan_pct,khan_votes])

    # Write the third row
    csvwriter.writerow([candidates[1],correy_pct,correy_votes])

    # Write the fourth row
    csvwriter.writerow([candidates[2],li_pct,li_votes])
    
    # Write the fifth row
    csvwriter.writerow([candidates[3], otooley_pct, otooley_votes])

    # Write the sixth row with the winner
    csvwriter.writerow(["Winner", "", candidates[max_index]])