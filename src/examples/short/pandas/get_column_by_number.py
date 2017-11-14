#!/usr/bin/env python

"""
This example shows how to get a column by number from a pandas
DataFrame.
"""

import pandas

df = pandas.read_csv(
    "/etc/passwd",
    sep=":",
    header=None, )
assert isinstance(df, pandas.core.frame.DataFrame)
num_rows = df.shape[0]

# lets get a series
c = df[0]
assert isinstance(c, pandas.core.series.Series)
assert c.shape == (num_rows,)

# another way
c = df[df.columns[0]]
assert isinstance(c, pandas.core.series.Series)
assert c.shape == (num_rows,)

# another way
c = df.loc[0]
assert isinstance(c, pandas.core.series.Series)
print(c.shape)
assert c.shape == (num_rows,)
