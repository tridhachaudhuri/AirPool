#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:23:15 2020

@author: tridhachaudhuri
"""


from pyflightdata import FlightData
import csv
api=FlightData()
#import pandas as pd

airport_iata=[]


with open('US_airlines.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            airport_iata.append(row[0])


#airport_iata=["LAX","JFK"]

header = ['airport_iata','url','avg_rating','total_rating','comment','author_facebookid','author_name',
          'timestamp_date','timestamp_time','number_of_reviews','number_of_evaluation']


file = open('airport_review.csv', 'a+', newline ='')
with file:
        writer = csv.writer(file)
        writer.writerow(header)
        file.close()

final=[]
for airport in airport_iata:
        #print(airport)
        details=api.get_airport_reviews(airport)
        #weather=api.get_airport_weather((airport))  
        #add this - imp
        try:
            url=details['url']
        except:
            url=""
        try: 
            avg_rating=details['ratings']['avg']
            total_rating=details['ratings']['total']
        except:
            avg_rating=""
            total_rating=""
        try:
            comment=details['comment'][0]['content']
        except:
            comment=""
        try:
            author_facebookid=details['comment'][0]['author']['facebookId']
            author_name=details['comment'][0]['author']['name']
        except:
            author_facebookid=""
            author_name=""
        try:
            timestamp_date=details['comment'][0]['timestamp_date']
            timestamp_time=details['comment'][0]['timestamp_time']
        except:
            timestamp_time=""
            timestamp_date=""
            
            
        number_of_reviews=details['reviews']
        number_of_evaluation=details['evaluation']
        
        row_list=[]
        
        row_list.append(airport)
        row_list.append(url)
        row_list.append(avg_rating)
        row_list.append(total_rating)
        row_list.append(comment)
        row_list.append(author_facebookid)
        row_list.append(author_name)
        row_list.append(timestamp_date)
        row_list.append(timestamp_time)
        row_list.append(number_of_reviews)
        row_list.append(number_of_evaluation)

        final.append(row_list)

    
file = open('airport_review.csv', 'a+', newline ='')

with file:
    writer = csv.writer(file)
    #writer.writerow(header)
    writer.writerows(final)
