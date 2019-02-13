import os
import csv

csvPath = "Resources/election_data.csv" 

voterIDs =[]
candidates = []

with open(csvPath, 'r') as csvFile:
    csvReader= csv.reader(csvFile, delimiter = ',')
    header = next(csvReader)

    for row in csvReader:
        voterIDs.append(int(row[0]))
        candidates.append(row[2])



total = len(voterIDs)

print(f'Total Votes: {total}')

candidateCount =[]
for candidate in set(candidates):
    candidateCount.append([candidate, candidates.count(candidate)])

percentage=[]
for row in candidateCount:
    print (f'{row[0]}: {round(((row[1]/total)*100),2)}% ({row[1]})')
    percentage.append(row[1]/total)

name = []
numofVotes= []

for row in candidateCount:
    name.append(row[0])
    numofVotes.append(row[1])

candidateZip = zip(name, numofVotes)
winnerVotes = max(numofVotes)

for row in candidateZip:
    if row[1] == winnerVotes:
        winnerName = row[0] 
print(f'Winner: {winnerName}')

# Specify the file to write to
output_path = "pypoll.csv"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as dataFile:

    # Initialize csv.writer
    csvwriter = csv.writer(dataFile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(['Candidate', 'Percentage', 'Votes/Candidate', 'Total Votes', 'Winner'])
    csvwriter.writerow([name, percentage, numofVotes, total, winnerName])

