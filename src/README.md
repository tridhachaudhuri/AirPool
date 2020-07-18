## Files in Repo

### job.py
  This is the main function that needs to run. Everything is initiallized and then eventually run within this function. It calls all the other python scripts  during their scheduled time after importing them. To schedule when the scripts needs to be called, the schedule package is used. Currently, the script is run once a day at around midnight. The script also performs multi-threading and all the other python scripts that are called through it are performed parallely. Each of the scripts that are to be called from the job.py file are put into its individual functions.  

### arrivalairports.py
  The script creates an object of the pyflight api and uses it to call the get_airport_arrivals(airport_name) function. The list of airport names are passed on to it from job.py. The raw JSON file for each airport is stored into the "raw data" S3 bucket. The code processes the data by parsing through the JSON and writing the needed information into individual CSV files for each airport. This CSV is then moved to the "processed data" S3 bucket. 

### departureairports.py
  The script creates an object of the pyflight api and uses it to call the get_airport_departures(airport_name) function. The list of airport names are passed on to it from job.py. The raw JSON file for each airport is stored into the "raw data" S3 bucket. The code processes the data by parsing through the JSON and writing the needed information into individual CSV files for each airport. This CSV is then moved to the "processed data" S3 bucket. 

### flighttoandfrom.py

  
### historyofflightsjob.py
  The script creates an object of the pyflight api and uses it to call the api.get_history_by_flight_number(airline_id) function. The list of airline_id are passed on to it from job.py. The raw JSON file for each airport is stored into the "raw data" S3 bucket. 
  
### awsupload.py

### country_info.py
  This script is run individually to get a list of all countries pyflight api holds information of. It creates an object of the pyflight api and uses it to call the get_countries() function which then returns a JSON file with all the needed countries and images of their flags. This data is then processed to a readable CSV format and the processed data is moved to the S3 bucket. 

### country_airport.py
  This script is run individually to keep a list of the airports that belong to a particular country. The country names can be found from the CSV extracted by the coutry_info.py script. Through this script, we are able to gain all the airports that belong to the U.S. and Canada. It creates an object of the pyflight api and uses it to call the get_airports(country_name) function which then returns a JSON file with all the airports belonging to a particular country. This data is then processed to a readable CSV format and the processed data is moved to the S3 bucket. 

### airport_review.py
  This script is run individually to keep a list of the reviews that belong to a individual aiports. The airport names can be found from the CSV extracted by the country_airport.py script. It creates an object of the pyflight api and uses it to call the get_airport_reviews(airport) function which then returns a JSON file with all the reviews and ratings belonging to a particular aiport. This data is then processed to a readable CSV format and the processed data is moved to the S3 bucket. 
  
### infoairport.py
  To get delay indexes, elevation, timezone etc of an aiport, we use the get_airport_details(airport) function to return a JSON file with all these information for a particular airport. The airport names can be found from the CSV extracted by the country_airport.py script. This data is then processed to a readable CSV format and the processed data is moved to the S3 bucket. 
  
### imagessave.py
  For each image URL link which consists in our database, the imagessave.py helps in extracting and storing image and gif using requests library in python. The code also extracts all pictures on Wikipedia for a search (airport names are searched) and save in S3 buckets. This is done by using the wikipedia library available in python.
