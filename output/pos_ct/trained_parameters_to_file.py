# !/usr/bin/env python

# Creating a dataframe out of json files with trained data parameters for each individual 
# Trying to create a multi indexed df 

import json
import pandas as pd
import glob
import re # python built-in package for working with regular expressions  
import os # for interacting with the operating system

# Using glob module to extract all files matching the pattern 
json_files = glob.glob("pos_ct/trained.*.phased.json")

all_data = []

for file in json_files:
    with open(file) as f:
        data=json.load(f)
        # print(data)
        # values=[data["state_names"], data["starting_probabilities"], data["transitions"], data["emissions"]]
        values = [data]
        all_data.extend(values)
        
for record in all_data:
    print(record)

# print(all_data)
