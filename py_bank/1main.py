# Number of months, Total, Change1, Change2, Average, Total Average,  Highest Profit, Highest Profit Date, Lowest profit, Lowest Profit date

N = 0
T = 0
C = 0
C2 = 1088983
A = 0
TS = 0
HP = 0
HPD = 0
LP = 0
LPD = 0

import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:

        # Collect Amounts

        C=int(row[1])
        A=C-C2
        TS = TS + A
        C2=int(row[1])
        N=N+1
        T+=int(row[1])

        if A>HP:
            HP = A
            HPD=row[0]

        if A<LP:
            LP = A
            LPD=row[0]



Avg_Change = TS/(N-1)

#print Amounts 
        
print("Financial Analysis") 
print("-------------------------")           
print("Total Months :  " + str(N))
print("Total:   $" + str(T))
print("Average Change:  $" + str(round(Avg_Change,2)))
print("Greatest increase in Profits: " + (HPD) +" ($"+ str(HP) +")")
print("Greatest Decrease in Profits: " + (LPD) +" ($"+ str(LP) +")")

# Specify the file to write to
output_path = os.path.join("..","py_bank","analysis", "new.txt")

f=open (output_path,"w+")

f.write("Financial Analysis\n")
f.write("------------------------\n")
f.write("Total Months : " + str(N)+"\n")
f.write("Total:   $" + str(T)+"\n")
f.write("Average Change:  $" + str(round(Avg_Change,2))+"\n")
f.write("Greatest increase in Profits: " + (HPD) +" ($"+ str(HP) +")\n")
f.write("Greatest Decrease in Profits: " + (LPD) +" ($"+ str(LP) +")\n")


    