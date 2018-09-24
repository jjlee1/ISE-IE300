import csv
import matplotlib.pyplot as plt


file=open('data.txt')
reader=csv.reader(file,delimiter=',')
next(reader)


data=[]

for line in reader:
    if int(line[1])>10:
        data.append(line)


customers=[]

for row in data:
    if row[0] not in customers:
        customers.append(row[0])
print(customers)
print('--------------')


AvgOrders=[]

for c in customers:
    TotalNum=0 #keeping track of total number of transactions for a given customer
    TotalQt=0 #computing total orderQt for a given customer
    for line in data:
        if c==line[0]:
            TotalQt+=int(line[1])
            TotalNum+=1
    AvgOrders.append(TotalQt/TotalNum)

print(AvgOrders)
print('----------------')


plt.bar(range(len(AvgOrder)), AvgOrders, align='center', color='r')
plt.xticks(range(len(AvgOrders)), customers)

plt.title("Average Order Quantity Plot")
plt.ylabel('Average Order Quantity')
plt.xlabel('Customers')

plt.show()








