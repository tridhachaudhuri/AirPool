#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 04:10:47 2020
@author: tridhachaudhuri
"""


#from pyflightdata import FlightData
import csv
#api=FlightData()
#import pandas as pd
import requests
"""
images=[]
with open('airport_info.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            #images.append(row[19])
            if row[19]!='':
                name="airportimages/png/"+row[0]+".png"
                uri=row[19]
                with open(name, 'wb') as f:
                     f.write(requests.get(uri).content)
            
"""

import wikipedia

with open('airport_info.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        lengthofimages=0
        if line_count == 0:
            line_count += 1
        else:
            #images.append(row[19])
            if row[1]!='':
                try:
                    wikipage = wikipedia.page(row[1])
                except:
                    continue
                lengthofimages=len(wikipage.images)
                for i in range(lengthofimages):
                    name="airportimages/wiki/"+row[0]+str(i)+".png"
                    uri=wikipage.images[i]
                    with open(name, 'wb') as f:
                        f.write(requests.get(uri).content)
