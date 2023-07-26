# !/usr/bin/env python

# Creating a dataframe out of json files with trained data parameters for each individual 
# Trying to create a multi indexed df 

import json
import pandas as pd
import glob
import re # python built-in package for working with regular expressions  
import os # for interacting with the operating system

# files = glob.glob('pos_ct/trained.*.phased.json')
# print(files)
# li = [] 

# for f in files:
#     temp_df = pd.read_csv(f)
#     li.append(temp_df)
#     print(f'Created df for {f} with shape {temp_df.shape}')

# # df = pd.concat(li, axis=0)
# # print(df.shape)
# # df.head()


trained_file_0 = "trained.HG00096.phased.json"
trained_file_1 = "trained.HG00097.phased.json"
trained_file_2 = "trained.HG00099.phased.json"
trained_file_3 = "trained.HG00100.phased.json"
trained_file_4 = "trained.HG00101.phased.json" 

trained_file_5 = "trained.HG00403.phased.json"
trained_file_6 = "trained.HG00404.phased.json"
trained_file_7 = "trained.HG00406.phased.json"
trained_file_8 = "trained.HG00407.phased.json"
trained_file_9 = "trained.HG00409.phased.json" 

json_df_0 = pd.read_json(trained_file_0)
json_df_1 = pd.read_json(trained_file_1)
json_df_2 = pd.read_json(trained_file_2)
json_df_3 = pd.read_json(trained_file_3)
json_df_4 = pd.read_json(trained_file_4)

json_df_5 = pd.read_json(trained_file_5)
json_df_6 = pd.read_json(trained_file_6)
json_df_7 = pd.read_json(trained_file_7)
json_df_8 = pd.read_json(trained_file_8)
json_df_9 = pd.read_json(trained_file_9)


df_list = [json_df_0, json_df_1, json_df_2, json_df_3, json_df_4, json_df_5, json_df_6, json_df_7, json_df_8, json_df_9]
df_index= ["HG00096", "HG00097", "HG00099", "HG00100", "HG00101", "HG00403", "HG00404", "HG00406", "HG00407", "HG00409"]

df_all = pd.concat(df_list, keys=df_index, names=['Individual_ID'])

print(df_all)

parameters_file = open("parameters_file.txt", 'w')
df_all.to_csv(parameters_file, sep='\t')