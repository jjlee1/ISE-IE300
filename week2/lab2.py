import csv

# Files to be read from and written to
inputfile='LabDemo.csv'
outputfile='out.txt'

# Open the file and advance it one line to ignore the header
inFile=open(inputfile,'r')
inReader=csv.reader(inFile)
next(inReader)

#Open the output text file to write the results
openout=open(outputfile,'w')

# Iterate through rest of the file and put data in a list called data
data=[]
for line in inReader:
    data.append(line)

print(data)
inFile.close()

# First if: Read all unique customers and sort them
# Second if: Read all unique SKUs and sort them
custnames=[]
SKUs=[]

for line in data:
    if line[0] not in custnames:
        custnames.append(line[0])
    if line[1] not in SKUs:
        SKUs.append(line[1])

custnames=sorted(custnames)
SKUs=sorted(SKUs)


for c in custnames:
    # Print customers name to begin their section of the output file
    print('Customer: ' + c)
    openout.write('Customer: ' + c+ '\n')
    # Initialize dictionaries for number sold and total price of each product for this customer
    totalPurchase={}
    totalMoney={}
    for s in SKUs:
        totalPurchase[s]=0
        totalMoney[s]=0
    # For each transaction (w/customer), update the number sold and total cost of the appropriate product
    for line in data:
        if line[0]==c:
            totalPurchase[line[1]]+= int(line[2])
            totalMoney[line[1]]+= int(line[2])*float(line[3])

# Print all product average prices (or 'No purchase history')
for s in SKUs:
    if totalPurchase[s]>0:
        round_avg = round(totalMoney[s]/totalPurchase[s],2)
            print("Average price for " + s + ':' + str(round_avg))
            openout.write("Average price for " + s + ':' + str(round_avg)+ '\n')
        else:
            print("Average Price for " + s + ':' + 'No Purchase History')
            openout.write("Average Price for " + s + ':' + 'No Purchase History'+ '\n')
# Print a blank line after each customer's average prices, for readability
print('')
    openout.write('\n')







