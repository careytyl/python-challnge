# Modules
import os
import csv


# Variable initialization
total_months = 0
net_total = 0
avg_change = 0
max_profit_num = 0
min_profit_num = 0


# Enter CSV path
csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath, newline="") as budget_data:
    budget = csv.reader(budget_data, delimiter=",")
    next(budget_data)


# Loop to read CSV file
    for row in budget:
        net_total = net_total + int(row[1]) # Adds/subtracts totals
        total_months += 1                   # Counts months/transactions

        if max_profit_num < int(row[1]):
            max_profit = row[0]             # Set to row[0] to pull the month/year of the greatest value in row[1]
        if min_profit_num > int(row[1]):
            min_profit = row[0]


avg_change = net_total / total_months       # Calculates average of transactions5

# Write to new CSV
output_file = os.path.join("..", "Output", "Financial Analysis.txt")

with open (output_file, 'w', newline='') as datafile:
	writer = csv.writer(datafile)
	writer.writerow(["Financial Analysis"])
	writer.writerow(["-----------------------------"])
	writer.writerow(["Total months: " + str(total_months)])
	writer.writerow(["Total: $" + str(net_total)])
	writer.writerow(["Average Change: ${:0.2f}".format(avg_change)])
	writer.writerow(["Greatest Increase in Profits: " + str(max_profit)])
	writer.writerow(["Greatest Decrease in Profits: " + str(min_profit)])

# Terminal output
print("Financial Analysis")
print("-------------------------------")
print("Total months: " + str(total_months))
print("Total: $" + str(net_total))
print("Average Change: ${:0.2f}".format(avg_change))
print("Greatest Increase in Profits: " + str(max_profit))
print("Greatest Decrease in Profits: " + str(min_profit))
