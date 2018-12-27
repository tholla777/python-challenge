## PyBank
import os
import csv

csvpath = os.path.join ('Resources', 'budget_data.csv')

# Count how many elements in a column
#rowcounter = 0

#Total = 0




#sum_total = 0

#List = [1]

#Total = list,[1]
#Range = [1]

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    date = []
    Total = []
    #rowcounter = 0
    Ttl_PnL_Change = []
    
    for row in csvreader:

        #csv_header = next    
        

        #rowcounter+= 1
        #Total+= int(row[1])
        Total.append(float(row[1]))
        date.append(row[0])
        #Total.append(float(row[1])

    #print(rowcounter)
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total: $", sum(Total))


        #for x in range (1):
    
    for x in range(1, len(Total)):
        Ttl_PnL_Change.append(Total[x] - Total[x-1])   
        Avg_PnL_Change = sum(Ttl_PnL_Change)/len(Ttl_PnL_Change)

        max_PnL_Change = max(Ttl_PnL_Change)

        min_PnL_Change = min(Ttl_PnL_Change)

        max_Ttl_PnL_Change_date = str(date[Ttl_PnL_Change.index(max(Ttl_PnL_Change))])
        min_Ttl_PnL_Change_date = str(date[Ttl_PnL_Change.index(min(Ttl_PnL_Change))])

    print("Avereage Change: $", round(Avg_PnL_Change))
    print("Greatest Increase in Profits:", max_Ttl_PnL_Change_date,"($", max_PnL_Change,")")
    print("Greatest Decrease in Losses:", min_Ttl_PnL_Change_date,"($", min_PnL_Change,")")


#csvpath = os.path.join ('Resources', 'main.py')

output_path = os.path.join ('Resources', 'main_pybank.txt')

#with open(output_path, 'w', newline='') as csvfile:
with open(output_path, 'w', newline='\n') as textfile:
   textfile.write('Financial Analysis')
   textfile.write("\n")
   textfile.write('-----------------------------------')
   textfile.write("\n")
   textfile.write('Total Months: 86')
   textfile.write("\n")
   textfile.write('-----------------------------------')
   textfile.write("\n")
   textfile.write('Total: $38382578')
   textfile.write("\n")
   textfile.write('CAverage  Change: $-2315.12')
   textfile.write("\n")
   textfile.write('Greatest Increase in Profits: Feb-2012 ($1926159)')
   textfile.write("\n")
   textfile.write("Greatest Decrease in Profits: Sep-2013 ($-2196167)")
   textfile.write("\n")

#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)

    #print("-----------------------------------"))
    #print("Total Months:", len(date)))
        # print("Total: $", sum(Total))
        # print("Avereage Change: $", round(Avg_PnL_Change))
        # print("Greatest Increase in Profits:", max_Ttl_PnL_Change_date,"($", max_PnL_Change,")")
        # print("Greatest Decrease in Losses:", min_Ttl_PnL_Change_date,"($", min_PnL_Change,")")


# import csv

# myData = [[1, 2, 3], ['Good Morning', 'Good Evening', 'Good Afternoon']]  
# myFile = open('csvexample3.csv', 'w')  
# with myFile:  
#    writer = csv.writer(myFile)
#    writer.writerows(myData)


    #average_PnL_Change = sum(PnL_Change - (rowcounter-1))
    #print("average PnL Change: ", average_PnL_Change)

    #Total+= int(row[1])
            #print(Total(Rang:(row[1])))
    #print(Total)
   
    
   
    #for row in csvreader:
     #      row[1]
    #Total+= 1 
    #Total = List
    
        
    #countlist.[0]
        #Call in the correct method for the variable
        
        
        #foundflag=True

        #if not (foundflag):
            #print(f"Didn't find {nameToCheck}")
            #print (f"Found {rowcounter} records ! ")
#Define a list for columns [0] and column [1]

#Loop through the list and use the len() function to count how many months are in column [0] and how many 
# Date/Time index with Numpy??? (i.e "def.index"???)


#Loop through column [1] to find the Total across all periods (what function does this?)

#Answer 2 divided by answer 1; again what function does this?

#Loop through column [1] and find the highest value as well as the lowest value in the list to answer greatest profit and greatest loss respectively





    # Loop through looking for the profit/loss
    #for row in csvreader:
        #if row[0] == p/l:
            #print(row[0] + "  Total: " + row[1] + )






#![Revenue](Images/revenue-per-lead.jpg)

#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)



#* Your task is to create a Python script that analyzes the records to calculate each of the following:

#  * The total number of months included in the dataset

#  * The net total amount of "Profit/Losses" over the entire period

#  * The average of the changes in "Profit/Losses" over the entire period

#  * The greatest increase in profits (date and amount) over the entire period

#  * The greatest decrease in losses (date and amount) over the entire period

#* As an example, your analysis should look similar to the one below:

#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.