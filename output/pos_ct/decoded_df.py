#!/usr/bin/env python

import pandas as pd

decoded1 = "HG02922.decoded.diploid.txt"
decoded2 = "HG00096.decoded.hap1.txt"

conv = {
    0: lambda x: "chr" + str(x), #adding chr to the chromosome number int he first column
    2: lambda x: int(x) + 1000, #adding a 1000 to the end position 
}

df_0 = pd.read_csv(decoded1, sep="\t", header=0, na_filter=False, converters=conv)
df_1 = pd.read_csv(decoded2, sep="\t", header=0, na_filter=False, converters=conv)

df_list = [df_0, df_1]
df_all = pd.concat(df_list)

print(df_all.tail)