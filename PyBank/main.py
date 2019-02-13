import os
import csv

csvPath = os.path.join("Resources", "budget_data.csv")

#Create empty lists
monthsList = []
profitlossesList = []

#Open and read file
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")
    header = next(csvReader)
    for row in csvReader:
        #Append first row to months list
        monthsList.append(row[0])
        #append profit losses to list as integers
        profitlossesList.append(int(row[1]))
        
#Calculate total number of months in list    
monthsLen = len(monthsList)
print(f'Total Months: {monthsLen}')

#Calculate total in profit losses list
total = 0
for row in profitlossesList:
    total += row
print(f'Total: ${total}')

#Net profit/losses over entire period and average change
#Set greatestInc to a very small number, so that any number will be added to the list when starting the for loop
greatestInc = 0

#Set greatestDec to a very large number, so that any number will be added to the list when starting the for loop
greatestDec = 999999999999999999

#For loop in range of the profit losses list to calculate change between each month, starting from thr second month, index 1
#Total change is the sum of the difference of profit/losses each month
totalChange = 0
for row in range(1,len(profitlossesList)):
    #Initially, take the difference from the current row and previous row, and set that to the greatestInc
    #If the next difference is greater than the previous difference, greatestInc is replaced with new calculated difference
    #Else if the difference is less than the previous difference, greatestDec is replaced with new calculated difference
    if profitlossesList[row] - profitlossesList[row-1] >= greatestInc:
        greatestInc = profitlossesList[row] - profitlossesList[row-1]
        greatestInc_month = monthsList[row]
    elif profitlossesList[row] - profitlossesList[row-1]<= greatestDec:
        greatestDec = profitlossesList[row] - profitlossesList[row-1]
        greatestDec_month = monthsList[row] 
    totalChange += (profitlossesList[row]- profitlossesList[row-1])

#Average of the changes between each month
numOfChanges = len(profitlossesList)-1
avgChange = round(totalChange/numOfChanges,2)
print(f'Average Change: ${avgChange}')
print(f'Greatest Increase in Profits: {greatestInc_month} (${greatestInc})')
print(f'Greatest Decrease in Profits: {greatestDec_month} (${greatestDec})')


# Specify the file to write to
output_path = "pybank.csv"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as dataFile:

    # Initialize csv.writer
    csvwriter = csv.writer(dataFile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits'])
    csvwriter.writerow([monthsLen, total, avgChange, [greatestInc_month, greatestInc], [greatestDec_month, greatestDec]])

