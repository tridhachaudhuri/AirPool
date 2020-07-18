#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 01:30:51 2020
@author: tridhachaudhuri
"""
from pyflightdata import FlightData
import csv
api=FlightData()

header = ['country','img']

file = open('country_list.csv', 'a+', newline ='')
with file:
        writer = csv.writer(file)
        writer.writerow(header)
        file.close()


details=api.get_countries()
final=[]
for d in details:
    country=d['country']
    img=d['img']
    row_list=[]
    row_list.append(country)
    row_list.append(img)
    
    final.append(row_list)

file = open('country_list.csv', 'a+', newline ='')

with file:
    writer = csv.writer(file)
    #writer.writerow(header)
    writer.writerows(final)
    
