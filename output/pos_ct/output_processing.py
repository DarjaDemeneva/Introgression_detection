# !/usr/bin/env python

import polars as pl
import glob 

decoded_files = glob.glob("GBR/*.decoded.hap*.txt")

# create list for storing df from each file 
dfs = []

# for each file extract pop and ID from the file name and add to each df 
for file in decoded_files[0:5]:
    file_name = file.split('.')[0]
    ind_id = file_name.split('/')[1]
    pop = file_name.split('/')[0]
    
    df = pl.read_csv(file, has_header=True, separator='\t')
    
    # Adding ID and pop to each df
    df_1 = df.with_columns( # with _columns to add columns to a data frame 
        (pl.lit(ind_id).alias("ID")), # pl.lit returns literal value pl.alias to name a column
        (pl.lit(pop).alias("pop")),
        (pl.col("end") + 1000) # adding 1000 to the end coordinate to match fragment length 
        )
    # print(df_1.head(5))

    dfs.append(df_1) # adding df to the dfs list 

# concatenating dfs from the list using align option to align dfs by column names 
decoded_df = pl.concat(dfs, how='align')

# Count archaic fragments with various mean_prob
count_per_interval = decoded_df.groupby(["ID", "mean_prob", "state"]).agg(pl.count("mean_prob").alias("count"))

# prob_count = decoded_df.groupby(["pop","ID", "state"])
print(count_per_interval.head(10))
# Count Archaic fragments out of all fragments

# print(decoded_df.head(5))