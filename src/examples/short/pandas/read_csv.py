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
