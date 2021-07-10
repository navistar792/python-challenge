import os
import csv
import locale

#Variables
locale.setlocale( locale.LC_ALL, '' )
tot_profit = 0
tot_months = 0
max_profit_delta = 0
min_profit_delta = 0
# initial value 867884
prior_mo_profit = 0
tot_profit_delta = 0

# Path to collect data from the Resources folder
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Use encoding for Windows
with open(pybank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip the header row
    next(csvreader)
        
    for row in csvreader:
        # set initial value for the prior month profit. Should just work for the first row
        if prior_mo_profit == 0:
            prior_mo_profit = int(row[1])
        # add the profit/loss for the row to the 'total' variable
        tot_profit = tot_profit + int(row[1])
        tot_months = tot_months + 1
        # get max profit by updating the variable if it's more than stored value
        if (int(row[1]) - prior_mo_profit) > max_profit_delta:
            max_profit_delta = (int(row[1]) - prior_mo_profit)
            max_profit_month = row[0]
        # get min profit by updating the variable if it's less than stored value
        if (int(row[1]) - prior_mo_profit) < min_profit_delta:
            min_profit_delta = (int(row[1]) - prior_mo_profit)
            min_profit_month = row[0]
        # calculate the change in profit for each month by comparing to the last month
        tot_profit_delta = tot_profit_delta+ (int(row[1]) - prior_mo_profit)
        # store the profit in this variable, to be used in the next iteration
        prior_mo_profit = int(row[1])    

# For learning purposes, define a function to print the results in athe terminal
def print_results():
    print("Financial Analysis")
    print ("------------------------------")
    print(f"Total Months: {tot_months}")
    print(f"Total: {locale.currency(tot_profit)}")
    print(f"Average Change: {locale.currency(tot_profit_delta/(tot_months-1))}")
    print(f"Greatest Increase in Profits: {max_profit_month} {locale.currency(max_profit_delta)}")
    print(f"Greatest Decrease in Profits: {min_profit_month} {locale.currency(min_profit_delta)}")

print_results()

# Specify the file to write to
output_path = os.path.join("Resources", "pybank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Metric Title', 'Month','Value'])

    # Write the second row
    csvwriter.writerow(['Total Months ','', tot_months ])

    # Write the third row
    csvwriter.writerow(['Total', '' ,locale.currency(tot_profit)])

    # Write the third row
    csvwriter.writerow(['Average Change','', locale.currency(tot_profit_delta/(tot_months-1))])

    # Write the fourth row
    csvwriter.writerow(['Greatest Increase in Profits', max_profit_month,locale.currency(tot_profit_delta/(tot_months-1))])

     # Write the fifth row
    csvwriter.writerow(['Greatest Decrease in Profits', min_profit_month,locale.currency(min_profit_delta)])