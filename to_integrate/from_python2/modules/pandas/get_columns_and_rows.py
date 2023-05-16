"""
This example shows how to know how many columns and rows a pandas
data frame has.
The idea is to use the "shape" method as it is the fastest.
There is no direct "rows" or "cols" methods.

References:
- https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
"""

import pandas

filename = "data_samples/3_by_2.tsv"
df = pandas.read_csv(
        filename,
        sep="\t",
        header=None,)
# df.shape is a tuple
assert df.shape == (3,2)
assert df.shape[0] == 3
assert df.shape[1] == 2
