import csv

myFile = open('FlightDelay.csv')
reader = csv.reader(myFile)
L = [i for i in reader][1:]



clean_list = []
with open('FlightTime.csv') as file:
    reader = csv.reader(file,delimiter=',')
    next(reader,None)
    # csv.list_dialects()
    for list in reader:
        if float(list[9]) > 100:
            clean_list.append(list)

for row in clean_list:
    print(row)
len(clean_list)


import csv
import statistics

FlightTime_list=[]
d = 1411.13
a = 33.4342
b = 41.9786
TFT = 0.117*d+0.517*(a-b)+43.2
dep_list = []

with open('FlightTime.csv') as file:
    reader = csv.reader(file,delimiter=',')
    next(reader,None)
    #csv.list_dialects()
    for list in reader:
       if float(list[9]) > 100:
           FlightTime_list.append(float(list[9]))
           dep_list.append(float(list[6]))

    print (sum(dep_list)/len(dep_list))


import csv
import statistics
import numpy as np

FlightTime_list=[]
AA_list = []
F9_list = []
NK_list = []
UA_list = []
US_list = []

with open('FlightTime.csv') as file:
    reader = csv.reader(file,delimiter=',')
    next(reader,None)
    #csv.list_dialects()
    for list in reader:
        if float(list[9]) > 100:
             FlightTime_list.append(float(list[9]))
             #$AA_list.append(list[1])
             #F9_list.append(list[1])
             #NK_list.append(list[1])
             #UA_list.append(list[1])
             # US_list.append(list[1])
             if list[1] == 'AA':
                 AA_list.append(float(list[9]))
             # if list[1] == 'F9':
                 # your code goes here, and go on...

    print ('The time added for AA airline is', (sum(AA_list)/len(AA_list)))
    # print ('The time added for AA airline is', (sum(F9_list)/len(F9_list)))

        # else:
            #if list[1] == 'F9':
                #print ('The time added for AA airline is', (sum(FlightTime_list)/len(FlightTime_list)))









infile=open('FlightTime.csv','r')
reader=csv.reader(infile)
next(reader,None)
flight_time_list=[]
dep_delay_list=[]
arr_delay_list=[]
AA_list=[]
F9_list=[]
UA_list=[]
US_list=[]
NK_list=[]

for row in reader:
    if (row[5]==''):
        row[5]=0
        row[6]=0
        row[7]=0
        row[8]=0
    # print row
    if (row[1]=="AA" and float(row[9])>100):
        AA_list.append(float(row[9]))
    if (row[1]=="F9" and float(row[9])>100):
        F9_list.append(float(row[9]) )
    if (row[1]=="UA" and float(row[9])>100):
        UA_list.append(float(row[9]))
    if (row[1]=="US" and float(row[9])>100):
        US_list.append(float(row[9]))
    if (row[1]=="NK" and float(row[9])>100):
        NK_list.append(float(row[9]))

    if (float(row[9])>100):
        dep_delay_list.append(float(row[6]))
        arr_delay_list.append(float(row[8]))
    # if float(row[9])>100:
        flight_time_list.append(float(row[9]))
num_obs=len(flight_time_list)
print ('the number of observations:',num_obs)

a=0.117*1411.13
b=0.517
c= 33.4342-41.9798
d=43.2
TFT=a+b*c+d

dep_avg=sum(dep_delay_list)/(len(dep_delay_list))
arr_avg=sum(arr_delay_list)/(len(arr_delay_list))

import pandas as pd
mydata = pd.read_csv('FlightTime.csv')
mydata2 = mydata.ix[mydata['Flight Time']>=100,:]

d = 1411.13
lambda_ori = 33.4342
lambda_des = 41.9786
TFT = (0.117 * d) + 0.517 * (lambda_ori - lambda_des) + 43.2
TT=TFT+dep_avg+arr_avg

AA_time_added=sum(AA_list)/len(AA_list)-TT
F9_time_added=sum(F9_list)/len(F9_list)-TT
UA_time_added=sum(UA_list)/len(UA_list)-TT
US_time_added=sum(US_list)/len(US_list)-TT
NK_time_added=sum(NK_list)/len(NK_list)-TT

# Departure average delay
departure_avg_delay = mydata2['Departure Delay'].mean()
arrival_avg_delay = mydata2['Arrival Delay'].mean()

typical_time = TFT + departure_avg_delay + arrival_avg_delay
grouped = mydata2['Flight Time'].groupby(mydata2['Carrier'])
time_added = grouped.mean() - typical_time
