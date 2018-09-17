#We use csv package to read any comma delimited files.
import csv

# First deifne the files to be read from and written to
inputfile='LabDemo.txt'  #We will use the LabDemo.csv that contains the comma separative values
outputfile='out.txt'

# Open the infile
inFile=open(inputfile,'r')
# Then we define the reader to read the file line by line.
inReader=csv.reader(inFile)
#and advance it one line to ignore the header using next fucntion
next(inReader)

# Open the outfile so that we can later write some results to this file
out=open(outputfile,'w')

# Now we define a list called myData and read each line from the input file and store to the myData list
# Then Iterate through rest of the file and put data in a list called mydata
# The reader will read the file line-by-line and append to the mydataList. Each line is the list of values (comma separated values) and the file is a list of lines.  (So, mayData is a list of list).
myData=[]
for line in inReader:
    myData.append(line)
#If you print it, we can see that each line is stored in the list.
print(myData)
#After reading and storing, we close the infile
inFile.close()

#now we want to write the first item of each line into the output file
#Iterate through the list and write the first item into the file.
#back slah n means once you write it move to the next line so that every item shows in new line for the readability.
for line in myData:
    print(line[0])
    out.write(line[0]+'\n')

# Dictionaries
# Dictionary is composed of key-value pairs. In other programming language like Java, this is a hash-map data structure. So, when I say key-value pair, these two are linked values where key is the unique identifier where we can find our data and the value is that data. In list, we identify teach item using index, but in dictionary we identify each value using key. In other word, list has index-item pair, and dictionary has key-value pair. List is defined using square bracket and dictionaries is defined using curly braces.


#The dictionary has following structure: dictionary_name = {key_1: value_1, key_2: value_2, key_3: value_3}
#For example, we can define
d = {'c': 'cat', 'd': 'dog'} # create a dictionary
print (d['c']) # print "cat"
#We can retrieve the value of dictionary by putting key in bracket, d[‘c’].
d['f'] = 'fish'
# d.pop('d')
del [d['d']] # remove an element from a dictionary

#We can also define dictionary as dict={} and put each key-value pair one by one like this.
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
print(dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

#You will need to use casting/rounding function to change the data type because when you read or write from and into the file the type should be string but when you compute them it should be numeric type.
x = 1  #integer
x=str(x) # cast any type to string
print(x+ 'hello')

#we can do the other way around
y='2'  #string
y=int(y) # cast any type to integer


z=3.141592
print(z)
z=round(z,2)
print(z)





