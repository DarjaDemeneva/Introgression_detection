#!/usr/bin/env python

# Parsing BED files (or other tab separated)

import numpy as np
import json

# To convert a text file to an array use np.loadtxt (if have missing values use np.genfromtxt). Skip the first header row.
array = np.loadtxt('1kgp_populations', delimiter="\t", dtype='str', skiprows=1)

# Create a dictionary to store ingroup and outgroup individuals
individuals = {
    "ingroup" : [],
    "outgroup" : []
}

ingroup_pop = ["HG00096", "HG00097", "HG00099", "HG00100", "HG02944"] # population selected as outgroup
outgroup_pop = ["YRI", "MSL", "ESN"] 

# Add outgroup individuals.
for row in array:
    #len_outgroup = 100 # number of outgroup individuals I want to analyse
    if row[1] in outgroup_pop: # and len(individuals['outgroup']) < len_outgroup
        individuals['outgroup'].append(row[0])

for row in array:
    #len_ingroup = 200
    if row[0] in ingroup_pop and row[0] not in individuals['outgroup']: 
        individuals['ingroup'].append(row[0])

# Creating a json file and adding the individuals dictionary to it.
# Will overwrite existing file
individuals_file = open('individuals.json', 'w')
individuals_file.write(json.dumps(individuals))
