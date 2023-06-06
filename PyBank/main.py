# import the os
import os
# import the csv file
import csv

# locate and open the csv file in read form
with open("resources/budget_data.csv", "r") as f:
    #reader = csv.reader(f)
    #budget_data = list(reader)
    total_months = 0
    average_profit = 0
    csvreader = csv.reader(f, delimiter = ',')
    
# skip the header
csv_header = next(csvreader)
print(f"CSV Header: {csv_header}")
nettotal = 0

# assign a title
title = "Financial Analysis"
print(title)
print("----------------------------------------")


    
for row in csvreader:
        print(row[1])
        nettotal += int(row[1])
        
print("The net total is:", nettotal)



# calculate the total number of months
#print("The total number of months:", total_months)
#total_months = len(budget_data)
#print("The total months:", total_months)

# calculate the total net of profit/losses
#def calculate_net(csv_file, column_name):
    #with open(csv_file, 'r') as file:
        #reader = csv.DictReader(file)
        #net_sum = 0
        

        #for row in reader:
           # net_value = float(row[column_name])
            #net_sum += net_value
        #return net_sum

#csv_file = 'budget_data.csv'
#column_name = 'Profit/Losses' 
#net_total = calculate_net(csv_file, column_name)
#print("Net Total:", net_total)

#net_pl = int(row[1]) 
#average_profit = (average_profit + net_pl) / total_months
#print(net_pl)
#print(average_profit)
#mylist = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
#print(mylist)

#print(mylist.index("Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"))
#total_netpl = 0
#for total_netpl in budget_data:
    #total_netpl += int(total_netpl)



# calculate the average of the changes in profit/losses
#average_pl = []
#for i in range(1, total_months):
    #average_pl.append(int(budget_data[i][1]) - int(budget_data[i - 1][1]))
# calculate the greatest increase in profit/losses with date and amount

# calculate the greatest decrease in profit/losses with date and amount


# export into text file
#output = ("analysis"):

