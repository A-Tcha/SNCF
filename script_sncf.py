# -*- coding: utf8 -*-

import re
from sys import exec_prefix
from unittest import expectedFailure
import requests
import pdb
import time
import datetime
import pickle
import csv
import urllib.request
from datetime import datetime, date, timedelta
import random
import pandas as pd
import json
import os
pd.options.mode.chained_assignment = None 


print("Script started.\n")

col_headers = ("datasetid",
    "recordid",
    "record_timestamp",
    "gc_obo_gare_origine_r_code_uic_c",
    #"gc_obo_date_heure_restitution_c",
    "gc_obo_type_c",
    "gc_obo_gare_origine_r_name",
    "gc_obo_nature_c",
    "gc_obo_nom_recordtype_sc_c",
    "date")

#create empty data frame
df1 = pd.DataFrame(columns = (col_headers))

count_checks = []




# url creation
url_1 = "https://ressources.data.sncf.com/api/records/1.0/search/"  \
    "?dataset=objets-trouves-restitution"                           \
    "&q="                                                           \
    "&rows=9999"                                                    \
    "&sort=date"                                                    \
    "&facet=date"                                                   \
    "&facet=gc_obo_date_heure_restitution_c"                        \
    "&facet=gc_obo_gare_origine_r_name"                             \
    "&facet=gc_obo_nature_c"                                        \
    "&facet=gc_obo_type_c"                                          \
    "&facet=gc_obo_nom_recordtype_sc_c"                             \
    "&refine.date="


# Define start and end date
start_date = date(2022, 1, 1)   # format date is YYYY-MM-DD 
end_date   = date(2022, 1, 10)  # format date is YYYY-MM-DD

delta = end_date - start_date




# Loop throught every date within date range selected
for i in range(delta.days + 1):
    
    day = start_date + timedelta(days = i)
    
    # date info extraction
    url_year = day.year
    url_month = day.month
    url_day = day.day

    # building full URL
    url_full = str(url_1) + str(url_year) + "%2F" + str(url_month) + "%2F"+ str(url_day)
    
    # make query
    request = requests.get(url_full)
    
    # get result
    q = request.json()
    
    # lenght of dataset
    nhits = q["nhits"] 
    
    count_checks.append(nhits)

    print("Data for", day, ":", nhits ,"records have been found.")


    # Get data and append them to dataframe
    i = 0
    while i < nhits:

        try:
        
            #print(i)

            new_row = pd.DataFrame(
                [
                    [
                    q["records"][i]["datasetid"],
                    q["records"][i]["recordid"],
                    q["records"][i]["record_timestamp"],
                    q["records"][i]["fields"]["gc_obo_gare_origine_r_code_uic_c"],
                    q["records"][i]["fields"]["gc_obo_type_c"],
                    q["records"][i]["fields"]["gc_obo_gare_origine_r_name"],
                    q["records"][i]["fields"]["gc_obo_nature_c"],
                    q["records"][i]["fields"]["gc_obo_nom_recordtype_sc_c"],
                    q["records"][i]["fields"]["date"]
                    ],  
                ], 
                    columns= (col_headers)
                    )

            # adding row to datafame
            df1 = pd.concat([df1, new_row], ignore_index = True, axis = 0)

        except:
            print("\n\tMissing data. Passing to next day:", i, "\n")

            pass

        i = i + 1


print("Lenght dataframe: ", len(df1))
print("Sum row counts: ", sum(count_checks))

#save data to pickle
with open('Data_SNCF.pickle', 'wb') as f:
    pickle.dump(df1, f)



df1.to_excel(r'INSERT YOUR PATH HERE') # example: df1.to_excel(r'C:\Users\user_name\Download\data_output.xlsx')

print("Script ended.")
