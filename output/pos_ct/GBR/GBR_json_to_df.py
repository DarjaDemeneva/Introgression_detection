# !/usr/bin/env python

import pandas as pd 
import numpy as np
import json 
import glob 

# Extracting IDs from each population  

with open("GBR_list.txt", "r") as GBR:
    individuals_GBR = GBR.read()
GBR_list = [i.strip() for i in individuals_GBR.split(",")]
GBR_list = [i.strip('"') for i in GBR_list]

# Using glob to extract all files matching the pattern
json_files = glob.glob("trained.*.phased.json")

# Empty list to store all dataframes generated from json files 
dfs = []
# Empty id_list for indexing each row with individual ID
id_list = []

# Loading json files into data frames and editing them 
for files in json_files:
    id_number = files.split('.')[-3] # extracting individual_id from file name 
    id_list.append(id_number)
    id_list.append(id_number) # append twice, because each state is used as a separate row for each individual
    df = pd.read_json(files)

# Adding each df to the list of dfs 
    dfs.append(df)

# Concatenating all dfs from the list into one df called temp    
temp = pd.concat(dfs)

# Adding individual IDs 
temp["ind_ID"] = id_list

# Defining a funciton to check if the ind_ID is in GBR_list
def get_population(id):
    if id in GBR_list:
        return "GBR"

# Adding a column with population based on ind_ID
temp["pop"] = temp["ind_ID"].apply(lambda x: get_population(x))       
# Setting ind_ID as the df index
temp.index = temp["ind_ID"]

print(temp)

# Saving 
temp.to_pickle("GBR_param_file.pkl")
# To read again > df = pd.read_pickle("param_file.pkl")