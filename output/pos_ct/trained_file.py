# Creating a dataframe out of json files with trained dat aparameters for each individual 
# Trying to create a multi indexed df to have 

import json
import pandas as pd


trained_file_0 = "trained.HG00096.phased.json"
trained_file_1 = "trained.HG00097.phased.json"
trained_file_2 = "trained.HG00099.phased.json"
trained_file_3 = "trained.HG00100.phased.json"
# trained_file_4 = 

json_df_0 = pd.read_json(trained_file_0)
# print(json_df_0)

json_df_1 = pd.read_json(trained_file_1)
# print(json_df_1)

json_df_2 = pd.read_json(trained_file_2)
# print(json_df_2)

json_df_3 = pd.read_json(trained_file_3)

df_list = [json_df_0, json_df_1, json_df_2, json_df_3]
df_index= ["HG00096", "HG00097", "HG00099", "HG00100"]

df_all = pd.concat(df_list, keys=df_index, names=['Individual_ID'])

print(df_all)

parameters_file = open("parameters_file.txt", 'w')
df_all.to_csv(parameters_file, sep='\t')