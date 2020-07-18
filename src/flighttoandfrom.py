#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 04:16:27 2020
@author: tridhachaudhuri
"""


from pyflightdata import FlightData
import csv
from datetime import date 
api=FlightData()


def writeheader(filename):
    header = ['to_airport','from_airport','number','callsign', 'live', 'text','type_Arrival','color','diverted',
          'utc_millis','utc_date','utc_time','utc',
          'local_date','local_time','model_code','model_name','registration',
          'country_name','country_alpha2','country_alpha3','airline_name','airline_iata','airline_icao',
          'origin_airport_name','origin_aiportcode_iata','origin_aiportcode_icao','origin_airport_latitude',
          'origin_airport_longitude','origin_airport_countryname','origin_airport_countrycode','origin_airport_city',
          'origin_aiporttimezone_name','origin_aiporttimezone_offset','origin_aiporttimezone_abbr','origin_aiporttimezone_abbrname',
          'dest_airport_name','dest_aiportcode_iata','dest_aiportcode_icao','dest_airport_latitude',
          'dest_airport_longitude','dest_airport_countryname','dest_airport_countrycode','dest_airport_city',
          'dest_airport_timezone_name','dest_airport_timezone_offset','dest_airport_timezone_abbr','dest_airport_timezone_abbrname',
          'scheduled_departuredate','scheduled_departuretime','scheduled_arrivaldate','scheduled_arrivaltime',
          'real_departuredate','real_departuretime','real_arrivaldate','real_arrivaltime']


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

def writeraw(flightdata,toairport,fromairport):
    parentpath=<path-to-save>+str(date.today())+"/flightstoandfrom/"
    file=str(toairport)+"_"+str(fromairport)+".txt"
    f1=open(parentpath+file,'w')
    if flightdata!=[]:
        f1.write(str(flightdata))
        
def apiarrivalfile(filename):
    
    airport_iata=['ATL','LAX','ORD','DFW','DEN','JFK','SFO','SEA','LAS','MCO','EWR','CLT','PHX','IAH','MIA','BOS','MSP','FLL','DTW','PHL','LGA','BWI','SLC','SAN','IAD','DCA','MDW','TPA','PDX','HNL','YYZ','MEX','YVR','YUL','CUN','YYC','BZE','SMF','PTY','GDL','SJO','MTY','YEG','SPR','TIJ','YOW','RIC','NAS','MEM','BOI','SDF','OKC','YHZ','CHS','MBJ','ORF', 'GEG','SAL','RNO','SBH','STT','CXH','KOA','GRR','POS','YWG','HAV','TUS','BHM','PVR','DAL','BNA','AUS','STL','SJC','HOU','OAK','MSY','RDU','MCI','SNA','SAT','CLE','RSW','IND','PIT','SJU','CVG','CMH','OGG','MKE','BDL','PBI','JAX','BUR','ABQ','ANC','BUF','ONT','OMA','ABR','ABI','CAK','FSD','LBB','IWS','FTW','PTK','AUK','KOT','ALS','ALB','PBG','PVD','ABY','CNM','AEX','ABE','AMA','AKP','MRI','ANI','ATW','AVL','ASE','QQR','PDK','ACY','BLM','AUO','AGS','EDC','AVP','BFL','BGR','BRW','BTR','BED','BLV','BLI','XNA','BET','BIL','BIS','BMI','TRI','BCT','BZN','BFD','BRD','BRO','BWD','SSI','QQY','BTV','BRL','BTM','CDW','CGI','CNM','CPR','CID','CMI','JZI','CRW','CHO','CHA','CYF','VAK','DPA','PWK']
    for toairport in airport_iata:
        for fromairport in airport_iata:
            if toairport!=fromairport:
                details=api.get_flights_from_to(toairport,fromairport)
                writeraw(details,toairport,fromairport)

                print(fromairport+","+toairport)
                if details==[]:
                    continue
                
                final=[]
    
                for i in range(len(details)):
                    number=details[i]['identification']['number']['default']
                    callsign=details[i]['identification']['callsign']
                    
                    live=details[i]['status']['live']
                    text=details[i]['status']['text']
                    
                    type_Arrival=details[i]['status']['generic']['status']['type']
                    color=details[i]['status']['generic']['status']['color']
                    diverted=details[i]['status']['generic']['status']['diverted']
                    
                    try:
                        utc_millis=details[i]['status']['generic']['eventTime']['utc_millis']
                    except:
                        utc_millis=""
                    try:
                        utc_date=details[i]['status']['generic']['eventTime']['utc_date']
                    except:
                        utc_date=""
                    try:
                        utc_time=details[i]['status']['generic']['eventTime']['utc_time']
                    except:
                        utc_time=""
                    
                    utc=details[i]['status']['generic']['eventTime']['utc']
                    
                    try:
                        local_date=details[i]['status']['generic']['eventTime']['local_date']
                    except:
                        local_date=""
                    try: 
                         local_time=details[i]['status']['generic']['eventTime']['local_time']
                    except:
                        local_time=""
                        
                        
                        
                    try:
                         model_code=details[i]['aircraft']['model']['code']
                    except:
                        model_code=""
                    try:
                        model_name=details[i]['aircraft']['model']['text']
                    except:
                        model_name=""
                    try:
                        registration=details[i]['aircraft']['registration']
                    except:
                        registration=""
                    try:
                        country_name=details[i]['aircraft']['country']['name']
                    except:
                        country_name=""
                    try:
                        country_alpha2=details[i]['aircraft']['country']['alpha2']
                    except:
                        country_alpha2=""
                    try:
                        country_alpha3=details[i]['aircraft']['country']['alpha3']
                    except:
                        country_alpha3=""

                    
                    try:
                        airline_name= details[i]['airline']['name']
                    except:
                        airline_name=""
                    try:
                        airline_iata=details[i]['airline']['code']['iata']
                    except:
                        airline_iata=""
                    try:
                        airline_icao=details[i]['airline']['code']['icao']
                    except:
                        airline_icao=""
                    
                    
                    origin_airport_name=details[i]['airport']['origin']['name']
                    origin_aiportcode_iata=details[i]['airport']['origin']['code']['iata']
                    origin_aiportcode_icao=details[i]['airport']['origin']['code']['icao']
                    
                    origin_airport_latitude=details[i]['airport']['origin']['position']['latitude']
                    origin_airport_longitude=details[i]['airport']['origin']['position']['longitude']
                    origin_airport_countryname=details[i]['airport']['origin']['position']['country']['name']
                    origin_airport_countrycode=details[i]['airport']['origin']['position']['country']['code']
                    origin_airport_city=details[i]['airport']['origin']['position']['region']['city']
                    
                    
                    origin_aiporttimezone_name=details[i]['airport']['origin']['timezone']['name']
                    origin_aiporttimezone_offset=details[i]['airport']['origin']['timezone']['offset']
                    origin_aiporttimezone_abbr=details[i]['airport']['origin']['timezone']['abbr']
                    origin_aiporttimezone_abbrname=details[i]['airport']['origin']['timezone']['abbrName']
    
                    
                    dest_airport_name=details[i]['airport']['destination']['name']
                    dest_aiportcode_iata=details[i]['airport']['destination']['code']['iata']
                    dest_aiportcode_icao=details[i]['airport']['destination']['code']['icao']
                    
                    dest_airport_latitude=details[i]['airport']['destination']['position']['latitude']
                    dest_airport_longitude=details[i]['airport']['destination']['position']['longitude']
                    dest_airport_countryname=details[i]['airport']['destination']['position']['country']['name']
                    dest_airport_countrycode=details[i]['airport']['destination']['position']['country']['code']
                    dest_airport_city=details[i]['airport']['destination']['position']['region']['city']
                    
                    dest_airport_timezone_name=details[i]['airport']['destination']['timezone']['name']
                    dest_airport_timezone_offset=details[i]['airport']['destination']['timezone']['offset']
                    dest_airport_timezone_abbr=details[i]['airport']['destination']['timezone']['abbr']
                    dest_airport_timezone_abbrname=details[i]['airport']['destination']['timezone']['abbrName']
                    
                    
                    scheduled_departuredate=details[i]['time']['scheduled']['departure_date']
                    scheduled_departuretime=details[i]['time']['scheduled']['departure_time']
                    scheduled_arrivaldate=details[i]['time']['scheduled']['arrival_date']
                    scheduled_arrivaltime=details[i]['time']['scheduled']['arrival_time']
                    
                    
                    try:
                        real_departuredate=details[i]['time']['real']['departure_date']
                        
                    except:
                        real_departuredate=""
                    try:
                        real_departuretime=details[i]['time']['real']['departure_time']
                        real_arrivaldate=details[i]['time']['real']['arrival_date']
                        real_arrivaltime=details[i]['time']['real']['arrival_time']
                    except:
                        real_departuretime=""
                        real_arrivaldate=""
                        real_arrivaltime=""
                        
                    
                    row_list=[]
                    
                    row_list.append(toairport)
                    row_list.append(fromairport)
                    
                    
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
                    
    
                    
                    row_list.append(airline_name)
                    row_list.append(airline_iata)
                    row_list.append(airline_icao)
    
                    
                    row_list.append(origin_airport_name)
                    row_list.append(origin_aiportcode_iata)
                    row_list.append(origin_aiportcode_icao)
                    
                    
                    row_list.append(origin_airport_latitude)
                    row_list.append(origin_airport_longitude)
                    row_list.append(origin_airport_countryname)
                    row_list.append(origin_airport_countrycode)
                    row_list.append(origin_airport_city)
                    
                    
                    row_list.append(origin_aiporttimezone_name)
                    row_list.append(origin_aiporttimezone_offset)
                    row_list.append(origin_aiporttimezone_abbr)
                    row_list.append(origin_aiporttimezone_abbrname)
                    
                    
                    row_list.append(dest_airport_name)
                    row_list.append(dest_aiportcode_iata)
                    row_list.append(dest_aiportcode_icao)
                    
                    row_list.append(dest_airport_latitude)
                    row_list.append(dest_airport_longitude)
                    row_list.append(dest_airport_countryname)
                    row_list.append(dest_airport_countrycode)
                    row_list.append(dest_airport_city)
                    
                    row_list.append(dest_airport_timezone_name)
                    row_list.append(dest_airport_timezone_offset)
                    row_list.append(dest_airport_timezone_abbr)
                    row_list.append(dest_airport_timezone_abbrname)
                    
                    
                    
                    row_list.append(scheduled_departuredate)
                    row_list.append(scheduled_departuretime)
                    row_list.append(scheduled_arrivaldate)
                    row_list.append(scheduled_arrivaltime)
                    
                    row_list.append(real_departuredate)
                    row_list.append(real_departuretime)
                    row_list.append(real_arrivaldate)
                    row_list.append(real_arrivaltime)
                    
                    final.append(row_list)
                writefile(final,filename)
