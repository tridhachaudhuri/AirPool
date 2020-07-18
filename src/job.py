#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 01:04:37 2020
@author: tridhachaudhuri
"""


import schedule
import time
import depatureairportjob
from datetime import date 
import csv
import arrivalairportjob
import os
import flighttoandfrom
import historyofflightsjob
import threading

    
def directorycreation():
    parentpath=<parent-path-to-create-folder>
    directory=str(date.today())
    path = os.path.join(parentpath, directory) 
    os.mkdir(path)
    
    parentpath=parentpath+str(date.today())+"/"
    directory="arrivals"
    path = os.path.join(parentpath, directory) 
    os.mkdir(path)
    
    directory="departure"
    path = os.path.join(parentpath, directory) 
    os.mkdir(path)
    
    directory="flighthistory"
    path = os.path.join(parentpath, directory) 
    os.mkdir(path)
    
    directory="flightstoandfrom"
    path = os.path.join(parentpath, directory) 
    os.mkdir(path)
    

def airport_iata(airports):
    with open('US_airlines.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                airports.append(row[0])
                
def airline_id(airlines):
    with open('/Users/tridhachaudhuri/Desktop/Insight/Code/pyflightdata/all_live_labels.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row!=[]:
                    airlines.append(row[0])
                
def departurejob(depairports):
    
    filename='airport_departure_US_'+str(date.today() )+'.csv'
    depatureairportjob.writeheader(filename)
    depatureairportjob.apidepartedfile(depairports,filename)
    
def arrivaljob(arriveairports):
    
    filename='airport_arrival_US_'+str(date.today() )+'.csv'
    arrivalairportjob.writeheader(filename)
    arrivalairportjob.apiarrivalfile(arriveairports,filename)
    
def flighttoandfromjob(fromtoairports):
    filename='fromtoairports_US_'+str(date.today() )+'.csv'
    flighttoandfrom.writeheader(filename)
    flighttoandfrom.apiarrivalfile(filename)
    
def flighthistoryjob(airlinesid):
    for airid in airlines:
        print(airid)
        historyofflightsjob.flights(airid)
        
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def job1():
    departurejob(airports)

def job2():
    arrivaljob(airports)
    
def job3():
    flighthistoryjob(airlines)

def job4():
    flighttoandfromjob(airports)

    
    
airports=[]    
airlines=[]
airport_iata(airports)
airline_id(airlines)
directorycreation()




schedule.every().day.at('00:01').do(run_threaded, job1)
schedule.every().day.at('00:01').do(run_threaded, job2)
schedule.every().day.at('01:44').do(run_threaded, job3)
schedule.every().day.at('00:01').do(run_threaded, job4)


while True:
    schedule.run_pending()
    time.sleep(1)
