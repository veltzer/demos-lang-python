"""
A basic demo of pandas
"""

from pandas import DataFrame

df = DataFrame(["a", "b", "c"], index=[0, 1, 2])
# print(df.get_values())  # noqa: ERA001  teaching: kept in the comment for the reader
print(df.loc[0])
print(df.loc[1])
print(df.loc[2])
print(df.xs(0))
print(df.xs(1))
print(df.xs(2))
