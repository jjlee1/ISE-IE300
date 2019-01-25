from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 3956 # Radius of earth (6371) in kilometers. Use 3956 for miles
    return c * r

print(haversine(-75.44041667,40.65236111,-99.68188889,32.41130556))

import csv

# Files to be read from and written to
inputfile1='all_airports.csv'
inputfile2='TypeAll_dis_BTS.csv'
outputfile='TypeAll_dis_BTS_Final.csv'

from collections import defaultdict
import csv
import re


with open(inputfile1) as f:
    reader = csv.reader(f,delimiter = ",")
    next(reader)
    airportLat = defaultdict(list)
    for line in reader:
        key = re.sub(r'\s+', '', line[0])
        valLat = line[1]
        valLong = line[2]
        airportLat[key].append(valLat)
        airportLat[key].append(valLong)
        print (airportLat)

with open(inputfile2) as f, open(outputfile, 'w') as f1:
    reader1 = csv.reader(f)
    writer1 = csv.writer(f1)
    next(reader1)
    for row in reader1:
        valuesToAppend=[]
        depAirport = re.sub(r'\s+', '', row[3])
        arrAirport = re.sub(r'\s+', '', row[5])
        if (airportLat.get(depAirport) is not None) and (airportLat.get(arrAirport) is not None):
            #lon1, lat1, lon2, lat2
            lat1 = float(airportLat.get(depAirport)[0])
            lon1 = float(airportLat.get(depAirport)[1])
            lat2 = float(airportLat.get(arrAirport)[0])
            lon2 = float(airportLat.get(arrAirport)[1])
            dist = int(int(haversine(lon1, lat1, lon2, lat2))*0.868976)
            valuesToAppend.append(str(dist))
        else:
            dist = -1
            valuesToAppend.append(str(dist))

        writer1.writerow(row+valuesToAppend)
