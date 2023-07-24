#Modules:
import os
import csv

#Path to collect data:
budget_data = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis","results.txt")

#Function to perform analysis of document: 
def pybankanalysis(filename):
        #Initialize variables
        totalmonths = 0
        net_total = 0
        final_value = 0
        last_value = 0

        #For each row in csv file:
        for row in csvreader:

            #Count total months:
            totalmonths = totalmonths + 1

            #Current change is current profit minus last value (0 for first line)
            current_change = int(row[1]) - last_value

            #To calculate net total, go row by row adding the profits
            net_total = net_total + int(row[1])

            #This if assigns starting values for some variables when reading the first line of the file:
            if totalmonths == 1:
                #starting value for average changes in profit/losses
                starting_value = int(row[1])
                #first greates increase and greatest decrease to compare later
                max_change = current_change
                min_change = current_change
                max_month = row[0]
                min_month = row[0]

            #this variable stores the profit in the current row as last value for the next loop:
            last_value = int(row[1])

            #compares to find greatest increase and greatest decrease:
            if current_change > max_change:
                #if current change is bigger, it's our new max
                max_change = current_change
                max_month = row[0]

            elif current_change < min_change:
                #if current change is smaller, this ir our new min
                min_change = current_change
                min_month = row[0]

        #Calculate the average change once we have read all rows:
        #sums the first and the last value and divides it between the total_months
        average_change = round(((last_value - starting_value) / (totalmonths-1)), 2)

        #saves results in a list:
        results= ["Financial Analysis",
            "--------------------------------",
            f"Total Months: {totalmonths}",
            f"Total: ${net_total}",
            f"Average Change: ${average_change}",
            f"Greatest Increase in Profits: {max_month} (${max_change})",
            f"Greatest Decrease in Profits: {min_month} (${min_change})"]
        
        #sends back the list of results
        return results

#Function to print and save in a txt file the contents of a list:
def print_and_save(output_file):
    with open(output_file, "w") as text:

        for line in results:
            text.write(f"{line}\n")
            print(f"{line}\n")


#Open and read CSV file
with open(budget_data, "r") as csvfile:

    #initialize csv reader
    csvreader = csv.reader(csvfile, delimiter = ",")

    #stores and skips header
    header = next(csvreader)

    #Perform analysis and receive results in a list:
    results = pybankanalysis(budget_data)

    #Print results and create txt file:
    print_and_save(output_file)