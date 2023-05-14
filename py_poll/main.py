# Total number of votes cast, votes for Charles, Diana, Raymon, % of vote for Charles, Diana, Raymon, Winner, Winner Name
T = 0
CCS = 0
DD = 0
RAD = 0
zCCS= 0
zDD = 0
zRAD = 0
W = 0
WN = 0

import os
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
   # print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader: 
        T=T+1
        if str(row[2]) == "Charles Casper Stockham":
            CCS = CCS+1
        elif str(row[2]) == "Diana DeGette":
            DD = DD+1
        else:
            RAD = RAD+1

zCCS= round((CCS/T)*100,3)
zDD = round((DD/T)*100,3)
zRAD = round((RAD/T)*100,3) 

def maximum(a,b,c):      
    List = [(CCS), (DD), (RAD)]
    return max(List)
    
W = (maximum((CCS),(DD),(RAD)))


print ("Election Results")
print ("--------------------------")
print ("Total Votes: " + str(T))
print ("--------------------------")
print ("Charles Casper Stockham: " + str(zCCS)+"% " +"(" +str(CCS)+")")
print ("Diana DeGette:  " + str(zDD)+"% "+"(" + str(DD)+")")
print ("Raymon Anthony Doane:  "+ str(zRAD)+"% "+"("  + str(RAD)+")")
print ("--------------------------")
if W == (CCS):
    print("Winner: Charles Casper Stockham")
elif W == (DD):
     print("Winner: Diana DeGette")
else:
     print("Winner: Raymon Anthony Doane")
print ("--------------------------")

# Specify the file to write to
output_path = os.path.join("..","py_poll","analysis", "new.txt")

f=open (output_path,"w+")

f.write("Election Results\n")
f.write("------------------------\n")
f.write("Total Votes: " + str(T)+"\n")
f.write("-------------------------\n")
f.write("Charles Casper Stockham: " + str(zCCS)+"% " +"(" +str(CCS)+")\n")
f.write("Diana DeGette:  " + str(zDD)+"% "+"(" + str(DD)+")\n")
f.write("Raymon Anthony Doane:  "+ str(zRAD)+"% "+"("  + str(RAD)+")\n")
f.write("-------------------------\n")
if W == (CCS):
    f.write("Winner: Charles Casper Stockham\n")
elif W == (DD):
     f.write("Winner: Diana DeGette\n")
else:
     f.write("Winner: Raymon Anthony Doane\n")
f.write("--------------------------")