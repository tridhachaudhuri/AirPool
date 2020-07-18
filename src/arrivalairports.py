#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 02:59:25 2020

@author: tridhachaudhuri
"""


from pyflightdata import FlightData
import csv
from datetime import date 
  

api=FlightData()

filename=''


def writeheader(filename):
    
            
    header = ['arrival_airport_iata','number','callsign', 'live', 'text','type_Arrival','color','diverted',
          'utc_millis','utc_date','utc_time','utc',
          'local_date','local_time','model_code','model_name','registration',
          'country_name','country_alpha2','country_alpha3','restricted','owner_name',
          'owner_iata','owner_icao','airline_name','airline_iata','airline_icao','airline_short',
          'origin_aiportcode_iata','origin_aiportcode_icao','origin_aiporttimezone_name','origin_aiporttimezone_offset','origin_aiporttimezone_abbr','origin_aiporttimezone_abbrname','origin_airport_terminal','origin_airport_baggage','origin_airport_gate','origin_airport_name','origin_airport_latitude','origin_airport_longitude','origin_airport_countryname','origin_airport_countrycode','origin_airport_city','dest_airport_timezone_name','dest_airport_timezone_offset','dest_airport_timezone_abbr','dest_airport_timezone_abbrname','dest_airport_terminal','dest_airport_baggage','dest_airport_gate','scheduled_departuredate','scheduled_departuretime','scheduled_arrivaldate','scheduled_arrivaltime',
          'real_departuredate','real_departuretime','estimated_arrivaldate','estimated_arrivaltime']


    file = open(filename, 'a+', newline ='')
    with file:
            writer = csv.writer(file)
            writer.writerow(header)
            file.close()
            
def writefile(final,filename):
    
    
    file = open(filename, 'a+', newline ='')
    
    with file:
        writer = csv.writer(file)
        writer.writerows(final)
        
def writeraw(flightdata,airport):
    parentpath=<path-to-save>+str(date.today())+"/arrivals/"
    file=str(airport)+".txt"
    f1=open(parentpath+file,'w')
    if flightdata!=[]:
        f1.write(str(flightdata))        

def apiarrivalfile(airport_iata,filename):
    
    for airport in airport_iata:
        LAXflights=api.get_airport_arrivals(airport, limit=100)
        print(airport)
        
    
        writeraw(LAXflights,airport)
        final=[]
    
        for i in range(len(LAXflights)):
            
            number=LAXflights[i]['flight']['identification']['number']['default']
            
            callsign=LAXflights[i]['flight']['identification']['callsign']
            live=LAXflights[i]['flight']['status']['live']
            text=LAXflights[i]['flight']['status']['text']
            type_Arrival=LAXflights[i]['flight']['status']['generic']['status']['type']
            color=LAXflights[i]['flight']['status']['generic']['status']['color']
            diverted=LAXflights[i]['flight']['status']['generic']['status']['diverted']
            
            try:
                utc_millis=LAXflights[i]['flight']['status']['generic']['eventTime']['utc_millis']
            except:
                utc_millis=""
            try:
                utc_date=LAXflights[i]['flight']['status']['generic']['eventTime']['utc_date']
            except:
                utc_date=""
            try:
                utc_time=LAXflights[i]['flight']['status']['generic']['eventTime']['utc_time']
            except:
                utc_time=""
            
            utc=LAXflights[i]['flight']['status']['generic']['eventTime']['utc']
            
            try:
                local_date=LAXflights[i]['flight']['status']['generic']['eventTime']['local_date']
            except:
                local_date=""
            try: 
                 local_time=LAXflights[i]['flight']['status']['generic']['eventTime']['local_time']
            except:
                local_time=""
            
            try:
                model_code=LAXflights[i]['flight']['aircraft']['model']['code']
            except:
                model_code=""
            try:
                model_name=LAXflights[i]['flight']['aircraft']['model']['text']
            except:
                model_name=""
            try:
                registration=LAXflights[i]['flight']['aircraft']['registration']
            except:
                registration=""
            try:
                country_name=LAXflights[i]['flight']['aircraft']['country']['name']
            except:
                country_name=""
            try:
                country_alpha2=LAXflights[i]['flight']['aircraft']['country']['alpha2']
            except:
                country_alpha2=""
            try:
                country_alpha3=LAXflights[i]['flight']['aircraft']['country']['alpha3']
            except:
                country_alpha3=""
            
            try:
                restricted=LAXflights[i]['flight']['aircraft']['restricted']
            except:
                restricted=""
            try:
                owner_name= LAXflights[i]['flight']['owner']['name']
            except:
                owner_name=""
            try:
                owner_iata=LAXflights[i]['flight']['owner']['code']['iata']
            except:
                owner_iata=""
            try:
                owner_icao=LAXflights[i]['flight']['owner']['code']['icao']
            except:
                owner_icao=""
            
            try:
                airline_name=LAXflights[i]['flight']['airline']['name']
            except: 
                airline_name=""
            try:
                airline_iata=LAXflights[i]['flight']['airline']['code']['iata']
            except:
                airline_iata=""
            try:
                airline_icao=LAXflights[i]['flight']['airline']['code']['icao']
            except:
                airline_icao=""
            try:
                airline_short=LAXflights[i]['flight']['airline']['short']
            except:
                airline_short=""
            
            
            origin_aiportcode_iata=LAXflights[i]['flight']['airport']['origin']['code']['iata']
            origin_aiportcode_icao=LAXflights[i]['flight']['airport']['origin']['code']['icao']
            origin_aiporttimezone_name=LAXflights[i]['flight']['airport']['origin']['timezone']['name']
            origin_aiporttimezone_offset=LAXflights[i]['flight']['airport']['origin']['timezone']['offset']
            origin_aiporttimezone_abbr=LAXflights[i]['flight']['airport']['origin']['timezone']['abbr']
            origin_aiporttimezone_abbrname=LAXflights[i]['flight']['airport']['origin']['timezone']['abbrName']
            origin_airport_terminal=LAXflights[i]['flight']['airport']['origin']['info']['terminal']
            origin_airport_baggage=LAXflights[i]['flight']['airport']['origin']['info']['baggage']
            origin_airport_gate=LAXflights[i]['flight']['airport']['origin']['info']['gate']
            origin_airport_name=LAXflights[i]['flight']['airport']['origin']['name']
            origin_airport_latitude=LAXflights[i]['flight']['airport']['origin']['position']['latitude']
            origin_airport_longitude=LAXflights[i]['flight']['airport']['origin']['position']['longitude']
            origin_airport_countryname=LAXflights[i]['flight']['airport']['origin']['position']['country']['name']
            origin_airport_countrycode=LAXflights[i]['flight']['airport']['origin']['position']['country']['code']
            origin_airport_city=LAXflights[i]['flight']['airport']['origin']['position']['region']['city']
            
            
            dest_airport_timezone_name=LAXflights[i]['flight']['airport']['destination']['timezone']['name']
            dest_airport_timezone_offset=LAXflights[i]['flight']['airport']['destination']['timezone']['offset']
            dest_airport_timezone_abbr=LAXflights[i]['flight']['airport']['destination']['timezone']['abbr']
            dest_airport_timezone_abbrname=LAXflights[i]['flight']['airport']['destination']['timezone']['abbrName']
            
            
            dest_airport_terminal=LAXflights[i]['flight']['airport']['destination']['info']['terminal']
            dest_airport_baggage=LAXflights[i]['flight']['airport']['destination']['info']['baggage']
            dest_airport_gate=LAXflights[i]['flight']['airport']['destination']['info']['gate']
            
            
            scheduled_departuredate=LAXflights[i]['flight']['time']['scheduled']['departure_date']
            scheduled_departuretime=LAXflights[i]['flight']['time']['scheduled']['departure_time']
            scheduled_arrivaldate=LAXflights[i]['flight']['time']['scheduled']['arrival_date']
            scheduled_arrivaltime=LAXflights[i]['flight']['time']['scheduled']['arrival_time']
            
            
            try:
                real_departuredate=LAXflights[i]['flight']['time']['real']['departure_date']
                
            except:
                real_departuredate=""
            try:
                real_departuretime=LAXflights[i]['flight']['time']['real']['departure_time']
            except:
                real_departuretime=""
            try:
                estimated_arrivaldate=LAXflights[i]['flight']['time']['estimated']['arrival_date']
            except:
                estimated_arrivaldate=""
            try:
                estimated_arrivaltime=LAXflights[i]['flight']['time']['estimated']['arrival_time']
            except:
                estimated_arrivaltime=""
            
            row_list=[]
            
            row_list.append(airport)
            row_list.append(number)
            row_list.append(callsign)
            row_list.append(live)
            row_list.append(text)
            row_list.append(type_Arrival)
            row_list.append(color)
            row_list.append(diverted)
            
            
            row_list.append(utc_millis)
            row_list.append(utc_date)
            row_list.append(utc_time)
            row_list.append(utc)
            row_list.append(local_date)
            row_list.append(local_time)
            
            
            row_list.append(model_code)
            row_list.append(model_name)
            row_list.append(registration)
            row_list.append(country_name)
            row_list.append(country_alpha2)
            row_list.append(country_alpha3)
            
            row_list.append(restricted)
            row_list.append(owner_name)
            row_list.append(owner_iata)
            row_list.append(owner_icao)
            
            
            row_list.append(airline_name)
            row_list.append(airline_iata)
            row_list.append(airline_icao)
            row_list.append(airline_short)
            
            row_list.append(origin_aiportcode_iata)
            row_list.append(origin_aiportcode_icao)
            row_list.append(origin_aiporttimezone_name)
            row_list.append(origin_aiporttimezone_offset)
            row_list.append(origin_aiporttimezone_abbr)
            row_list.append(origin_aiporttimezone_abbrname)
            row_list.append(origin_airport_terminal)
            row_list.append(origin_airport_baggage)
            row_list.append(origin_airport_gate)
            row_list.append(origin_airport_name)
            row_list.append(origin_airport_latitude)
            row_list.append(origin_airport_longitude)
            row_list.append(origin_airport_countryname)
            row_list.append(origin_airport_countrycode)
            row_list.append(origin_airport_city)
            
            
            row_list.append(dest_airport_timezone_name)
            row_list.append(dest_airport_timezone_offset)
            row_list.append(dest_airport_timezone_abbr)
            row_list.append(dest_airport_timezone_abbrname)
            
            
            row_list.append(dest_airport_terminal)
            row_list.append(dest_airport_baggage)
            row_list.append(dest_airport_gate)
            
            
            row_list.append(scheduled_departuredate)
            row_list.append(scheduled_departuretime)
            row_list.append(scheduled_arrivaldate)
            row_list.append(scheduled_arrivaltime)
            
            row_list.append(real_departuredate)
            row_list.append(real_departuretime)
            row_list.append(estimated_arrivaldate)
            row_list.append(estimated_arrivaltime)
            final.append(row_list)
    
        writefile(final,filename)

                    
            
