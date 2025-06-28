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
# pylint: disable=unsubscriptable-object, no-member
c1 = df[0]
assert isinstance(c1, pandas.core.series.Series)
assert c1.shape == (num_rows,)

# another way
c2 = df[df.columns[0]]
assert isinstance(c2, pandas.core.series.Series)
assert c2.shape == (num_rows,)

# another way
c3 = df.loc[0]
assert isinstance(c3, pandas.core.series.Series)
print(c3.shape)
assert c3.shape == (num_rows,)
