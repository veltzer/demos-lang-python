"""
A demo of how to load a csv file
"""

import pandas as pd

df = pd.read_csv(
    "/etc/passwd",
    sep=":",
    header=None, )
print(df)
print(df.shape)
# show that the second column is actually a "C" type integer
