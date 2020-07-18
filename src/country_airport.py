#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 01:40:30 2020
@author: tridhachaudhuri
"""


from pyflightdata import FlightData
import csv
api=FlightData()
#import pandas as pd

airport_iata=[]

with open('country_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            airport_iata.append(row[0])
            
header = ['country','name','iata', 'lat','lon']

file = open('country_airport.csv', 'a+', newline ='')
with file:
        writer = csv.writer(file)
        writer.writerow(header)
        file.close()
        

for country in airport_iata:
    final=[]
    details=api.get_airports(country)
    for d in details:
        name=d['name']
        iata=d['iata']
        lat=d['lat']
        lon=d['lon']
        
        row_data=[]
        
        row_data.append(country)
        row_data.append(name)
        row_data.append(iata)
        row_data.append(lat)
        row_data.append(lon)
        
        final.append(row_data)
    
    file = open('country_airport.csv', 'a+', newline ='')
    
    with file:
        writer = csv.writer(file)
        #writer.writerow(header)
        writer.writerows(final)
