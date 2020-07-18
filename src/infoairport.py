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

header = ['airport_iata','name','iatacode','icaocode','delayindex_arrivals','delayindex_departures','stats',
          'latitude','longitude','elevation_m','elevation_ft','timezone_name','timezone_offset',
          'timezone_abbr','timezone_abbrname','url_homepage','url_webcam','url_wiki','img_src','img_link',
          'img_source','visible']


file = open('airport_info.csv', 'a+', newline ='')
with file:
        writer = csv.writer(file)
        writer.writerow(header)
        file.close()

final=[]
for airport in airport_iata:
    try:
        details=api.get_airport_details(airport)
        #weather=api.get_airport_weather((airport))  
        #add this - imp
        name=details['name']
        
        iatacode=details['code']['iata']
        icaocode=details['code']['icao']
        delayindex_arrivals=details['delayIndex']['arrivals']
        delayindex_departures=details['delayIndex']['departures']
        stats=details['stats']
        
        latitude=details['position']['latitude']
        longitude=details['position']['longitude']

        try:
            elevation_m=details['position']['elevation']['m']
        except:
            elevation_m=""
        try:
            elevation_ft=details['position']['elevation']['ft']
        except:
            elevation_ft=""

        timezone_name=details['timezone']['name']
        timezone_offset=details['timezone']['offset']
        timezone_abbr=details['timezone']['abbr']
        timezone_abbrname=details['timezone']['abbrName']
        
        url_homepage=details['url']['homepage']
        url_webcam=details['url']['webcam']
        url_wiki=details['url']['wikipedia']
        
        try:
            img_src=details['airportImages']['large'][0]['src']
        except:
            img_src=""
        try:
            img_link=details['airportImages']['large'][0]['link']
        except:
            img_link=""
        try:
            img_source=details['airportImages']['large'][0]['source']
        except:
            img_source=""
        
        visible=details['visible']
        
        row_list=[]
        
        row_list.append(airport)
        row_list.append(name)
        row_list.append(iatacode)
        row_list.append(icaocode)
        row_list.append(delayindex_arrivals)
        row_list.append(delayindex_departures)
        row_list.append(stats)
        row_list.append(latitude)
        row_list.append(longitude)
        row_list.append(elevation_m)
        row_list.append(elevation_ft)
        row_list.append(timezone_name)
        row_list.append(timezone_offset)
        row_list.append(timezone_abbr)
        row_list.append(timezone_abbrname)
        row_list.append(url_homepage)
        row_list.append(url_webcam)
        row_list.append(url_wiki)
        row_list.append(img_src)
        row_list.append(img_link)
        row_list.append(img_source)
        row_list.append(visible)
        final.append(row_list)
    except:
        print(airport)
    
file = open('airport_info.csv', 'a+', newline ='')

with file:
    writer = csv.writer(file)
    #writer.writerow(header)
    writer.writerows(final)
