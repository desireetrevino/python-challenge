#Modules:
import os
import csv

#Path to collect data:
budget_data = os.path.join("..", "Resources", "budget_data.csv")
output_file = os.path.join("results.txt")

#List to store analysis:
results = []
profits = {}

#Read CSV file
with open(budget_data, "r") as csvfile:

    #initialize csv reader
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header
    next(csvreader)

    #initialize variables
    totalmonths = 0
    net_total = 0
    final_value = 0
    last_value = 0

    #Call functions to perform different calculations
    for row in csvreader:

        #stores values in a dictionary
        profits[row[0]] = int(row[1])
        totalmonths = totalmonths + 1
        current_change = int(row[1]) - last_value

        #To calculate net total, go row by row adding the profits
        net_total = net_total + int(row[1])

        #This if assigns starting values for some variables we need:
        if totalmonths == 1:
            #starting value for average changes in profit/losses
            starting_value = int(row[1])
            max_change = current_change
            min_change = current_change
            max_month = row[0]
            min_month = row[0]

        #this variable will keep the value of the last row before exiting the for loop
        last_value = int(row[1])

        #checks for greatest increase and greatest decrease
        if current_change > max_change:
            max_change = current_change
            max_month = row[0]
        elif current_change < min_change:
            min_change = current_change
            min_month = row[0]

    #Calculate the average change once we have read all rows:
        #sums the first and the last value and divides it between the total_months

    average_change = round(((last_value - starting_value) / (totalmonths-1)), 2)

#Print analysis and export text file with results

#print results
results= ["Financial Analysis",
          "--------------------------------",
          f"Total Months: {totalmonths}",
          f"Total: ${net_total}",
          f"Average Change: ${average_change}",
          f"Greatest Increase in Profits: {max_month} (${max_change})",
          f"Greatest Decrease in Profits: {min_month} (${min_change})"]

#create and write txt file, this part of the code is based on an example given by Reed
with open(output_file, "w") as text:

    for line in results:
        text.write(f"{line}\n")
        print(f"{line}\n")



    #export results to txt file using dictionary