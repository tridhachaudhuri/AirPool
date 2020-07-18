#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 04:41:49 2020
@author: tridhachaudhuri
"""


from pyflightdata import FlightData
from datetime import date 


api=FlightData()


def file_creator(details,airline):
    fname="<path-to-save>"+str(date.today())+"/flighthistory/"+str(airline)+'.txt'
    file = open(fname, 'w')
    if details!=[]:
        file.write(str(details))

def flights(airlinesid):
    try:
        details=api.get_history_by_flight_number(str(airlinesid)) 
    except TypeError:
       details=[]
    file_creator(details,airlinesid)
