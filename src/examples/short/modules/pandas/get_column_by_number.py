"""
This example shows how to get a column by number from a pandas
DataFrame.
"""

import pandas as pd

df = pd.read_csv(
    "/etc/passwd",
    sep=":",
    header=None, )
assert isinstance(df, pd.DataFrame)
num_rows = df.shape[0]

# lets get a series
c1 = df[0]
assert isinstance(c1, pd.Series)
assert c1.shape == (num_rows,)

# another way
c2 = df[df.columns[0]]
assert isinstance(c2, pd.Series)
assert c2.shape == (num_rows,)

# another way
c3 = df.loc[0]
assert isinstance(c3, pd.Series)
print(c3.shape)
assert c3.shape == (num_rows,)
