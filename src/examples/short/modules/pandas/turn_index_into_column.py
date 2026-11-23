"""
This is an example of how to turn an index into a column in pandas

References:
- https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column
"""

import pandas as pd

filename = "shared-samples/tsv/2_by_2.tsv"
df = pd.read_csv(
    filename,
    sep="\t",
    header=None,
)

print(df.head())

df = df.set_index(0)
print(df.head())

df = df.reset_index(level=0)
print(df.head())
