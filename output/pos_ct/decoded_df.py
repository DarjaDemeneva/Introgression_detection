#!/usr/bin/env python

# Using Pandas to edit decoded files and concatenate them into one
# prefer using bash, so have stopped working on this file 

import pandas as pd

decoded1 = "HG02922.decoded.diploid.txt"
decoded2 = "HG00096.decoded.hap1.txt"

# converter to use when loading files into dataframe; performs operations on specific columns 
conv = {
    0: lambda x: "chr" + str(x), # adding chr to the chromosome number in the first column
    2: lambda x: int(x) + 1000, # adding a 1000 to the end position 
}

df_0 = pd.read_csv(decoded1, sep="\t", header=0, na_filter=False, converters=conv)
df_1 = pd.read_csv(decoded2, sep="\t", header=0, na_filter=False, converters=conv)

df_list = [df_0, df_1]
df_all = pd.concat(df_list)

print(df_all.tail)