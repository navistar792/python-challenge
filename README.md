# python-challenge

* Note: For learning purposes, I added sample code using pictures and pasting code.

## PyBank Overview

1. Utilize the os and csv packages
    * The [os module](https://docs.python.org/3/tutorial/stdlib.html) provides functionality for interacting with the operating system, such as opening and reading csv files
    * The [csv module](https://docs.python.org/3/library/csv.html) is used for importing and exporting files in the csv format
    * The [locale module](https://docs.python.org/3/library/locale.html)

2. Declare key variables to sum the profit and count the months as the code iterates through the data. Initial value is set to zero

3. Connect to the budget_data.csv using the os.path.join() method, and open it. The first path argument is omitted, since the csv file is in a subfolder (\Resources) of the same directory as Main.py.
 
![Image#2](https://github.com/navistar792/python-challenge/blob/main/PyBank/Resources/connection.jpg)

4. Iterate through the data. For each row:
    * Add the profit to the total
    * Add one to the month count
    * Calculate the max profit by determining if the current profit value is greater than the last value, and if so, storing it in the designated variable
    * Calculate the min profit by determining if the current profit is lower than the prior value, and if so, storing it in the designated variable 
    * Update the prior month's profit with the current month, to be used in the next iteration 
        ![Image #3](https://github.com/navistar792/python-challenge/blob/main/PyBank/Resources/iterate.jpg)

5. Print the results to the terminal. Define a function for this step, for purposes of learning  
    ![Image #4](https://github.com/navistar792/python-challenge/blob/main/PyBank/Resources/results.jpg)

6.  Export the results to a csv file. Three columns were included
    * First column describes the metric (e.g. "average change")
    * The second column lists the month, if relevant
    * The third column lists totals
![Image #5](https://github.com/navistar792/python-challenge/blob/main/PyBank/Resources/output.jpg)   

## PyPoll Overview    

1. Utilize the os and csv packages
    a. The [os module](https://docs.python.org/3/tutorial/stdlib.html) provides functionality for interacting with the operating system, such as opening and reading csv files
    b. The [csv module](https://docs.python.org/3/library/csv.html) is used for importing and exporting files in the csv format

2. Declare key variables to tally the votes as the code iterates through the data. Initial value is set to zero

3. Establish two lists: one for the candidates, and one to store their total votes. These lists will be used later to help count votes by candidates, and to determine the winner.

4. Connect to the election_data.csv using the os.path.join() method, and open it. The first path argument is omitted, since the csv file is in a subfolder (\Resources) of the same directory as Main.py.

5. Iterate through the data to calulate total votes and the total votes by candidate 
    a. For each iteration, add one vote to the total votes (tot_votes)
    b. the candidates' names are in the third column. Use if statements to count the votes for each candidate, adding a vote if their name matches.
    c. use an else statement to tally any votes that don't match the four candidates (hint: there weren't any "other" votes in this dataset)
    ![Image #1](https://github.com/navistar792/python-challenge/blob/main/PyPoll/Resources/iteration.jpg)

6. Append the total votes for each candidate to the candidate votes <b>(cand_votes)</b> list.

7. To make the print results code easier to read: 
    a. calculate all the percentages needed for the output
    b. calculate the candidate with the max number of votes
    ![Image #6](https://github.com/navistar792/python-challenge/blob/main/PyPoll/Resources/calculations.jpg)

8. create a function that, when called, prints the results to the terminal. From a design perspective, no calculations were done within the print statements - everything was pre-calculated using variables: 

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

9. Export the results to a csv file. Three columns were included
    a. First column describes the metric (e.g. "total votes")
    b. The second column lists percentages, if available
    c. The third column lists totals, such as total votes, including votes by candidate 

        # results output to a file
        # Specify the file to write to
        output_path = os.path.join("Resources", "pypoll.csv")
        # Open the file using "write" mode. Specify the variable to hold the contents
        with open(output_path, 'w', newline='') as csvfile:
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')
            
            # Write the first row (column headers)
            csvwriter.writerow(['Description', '%','Votes'])

            # Write the second row
            csvwriter.writerow(['Total Votes ','', tot_votes])


