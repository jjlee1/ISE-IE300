
# Demo Code: Modified Example 1
#     Origin  Destination Airline  Departure Delay  Arrival Delay
# 0    DFW         ORD   Delta                5             11
# 1    DFW         ORD   Delta                4              4
# 2    DFW         ORD   Delta                8              8
# 3    LAX         ORD   Delta                1              2
# 4    LAX         ORD  United                7              9
# 5    LAX         LGA  United               -2              2
# 6    LAX         LGA  United                6             10
# 7    LAX         LGA   Delta               -3             -2
# 8    DFW         LGA  United                0              2
# 9    DFW         ORD  United                8              9
####---------------for loop---------------------###

import csv
infile = open('Example1.csv', 'r')
reader = csv.reader(infile)
next(reader, None) # skip the headers

delaydata = [] # save data to a list
for row in reader:
    delaydata.append(row)

originList = [] # find p = 1/(# of possible values for each column)
for row in delaydata:
    originList.append(row[0]) # Column 1: Origin
p_origin = 1/len(set(originList))

# initialization
count_Y = 0 # number of Y
count_DFW_Y = 0 # number of DFW and Y
count_LGA_Y = 0 # number of LGA and Y
count_Delta_Y = 0 # number of Delta and Y

count_N = 0 # number of N
count_DFW_N = 0 # number of DFW and N
count_LGA_N = 0 # number of LGA and N
count_Delta_N = 0 # number of Delta and N

# find total time
for row in delaydata:
    total_delay = float(row[3]) + float(row[4]) # column indices might be different in case study
    if total_delay > 15:
        count_Y += 1
        if row[0] == "DFW":
            count_DFW_Y += 1
        if row[1] == "LGA":
            count_LGA_Y += 1
        if row[2] == "Delta":
            count_Delta_Y += 1
    else:
        count_N += 1
        if row[0] == "DFW":
            count_DFW_N += 1
        if row[1] == "LGA":
            count_LGA_N += 1
        if row[2] == "Delta":
            count_Delta_N += 1

print("count_Y =", count_Y)
print("count_DFW_Y =", count_DFW_Y)
print("count_LGA_Y =", count_LGA_Y)
print("count_Delta_Y =", count_Delta_Y)

# Then calculate probabilities on your own ...

####-------------- pandas ---------------------###
import pandas as pd
# read csv
# mydata = pd.read_csv('C:\\Users\\Tinghao\\Dropbox\\IE300 Fall2015\\Week of 9.21\\Example1.csv')
# mydata = pd.read_csv('E:\\Dropbox\\IE300 Fall2015\\Week of 9.21\\Example1.csv')
mydata = pd.read_csv("Example1.csv")

# compute total delay
mydata["Total Delay"] = mydata['Departure Delay'] + mydata['Arrival Delay']

# assign Y and N
mydata["Yes or No"] = "NA" # set a default value
mydata.ix[mydata["Total Delay"] >= 15, "Yes or No"] = "Y"
mydata.ix[mydata["Total Delay"] < 15, "Yes or No"] = "N"

# find probability p for each column: p = 1/(# of possible values for each column)
p_origin = 1/ len(pd.unique(mydata.Origin.ravel())) # two airlines: Delta & United
p_destination = 1 / len(pd.unique(mydata.Destination.ravel())) # two origins: DFW, LAX
p_airline = 1/ len(pd.unique(mydata.Airline.ravel())) # two destinations: ORD, LGA

Y_or_N =  mydata.groupby(["Yes or No"]).size() 
count_N = Y_or_N[0]; count_Y = Y_or_N[1]
prob_N = count_N /(count_N + count_Y)
prob_Y = 1 - prob_N

origin_Y_or_N = mydata.groupby(['Origin', "Yes or No"]).size()
count_DFW_N = origin_Y_or_N[0] 
count_DFW_Y = origin_Y_or_N[1]

destimation_Y_or_N = mydata.groupby(['Destination', "Yes or No"]).size()
count_LGA_N = destimation_Y_or_N[0]
count_LGA_Y = destimation_Y_or_N[1]

airline_Y_or_N = mydata.groupby(['Airline', "Yes or No"]).size()
count_Delta_N = airline_Y_or_N[0]
count_Delta_Y = airline_Y_or_N[1]

# calculate probabilities
m = 3 # m = 3 is given
prob_DFW_given_Y = (count_DFW_Y + m * p_origin) / (count_Y + m) # P(DFW | Y)
prob_LGA_given_Y = (count_LGA_Y + m * p_destination) / (count_Y + m) # P(LGA | Y)
prob_Delta_given_Y = (count_Delta_Y + m * p_airline) / (count_Y + m) # P(Delta | Y)
prob_Y_given_DFW_LAX_Delta = prob_Y * prob_DFW_given_Y * prob_LGA_given_Y * prob_Delta_given_Y # P(Y | DFW, LGA, Delta)

prob_LGA_given_N = (count_LGA_N + m * p_destination) / (count_N + m) # P(LGA | N)
prob_DFW_given_N = (count_DFW_N + m * p_origin) / (count_N + m) # P(DFW | N)
prob_Delta_given_N = (count_Delta_N + m * p_airline) / (count_N + m) # P(Delta | N)
prob_N_given_DFW_LAX_Delta = prob_N * prob_DFW_given_N * prob_LGA_given_N * prob_Delta_given_N # P(N | DFW, LGA, Delta)

result = "Y" if prob_Y_given_DFW_LAX_Delta >= prob_N_given_DFW_LAX_Delta else "N"
print("Since y_hat = argmax{", prob_Y_given_DFW_LAX_Delta, prob_N_given_DFW_LAX_Delta, "} =", max(prob_Y_given_DFW_LAX_Delta, prob_N_given_DFW_LAX_Delta))
print("we classify DFW-LGA on Delta as", result)

