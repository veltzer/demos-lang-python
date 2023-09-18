"""
A demo of how to load a csv file
"""

import pandas

df = pandas.read_csv(
    "/etc/passwd",
    sep=":",
    header=None, )
print(df)
print(df.shape)
# show that the second column is actually a "C" type integer
