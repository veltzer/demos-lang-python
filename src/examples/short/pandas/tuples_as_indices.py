"""
A basic demo of pandas
"""

from pandas import DataFrame

df = DataFrame(["a", "b", "c"], index=[("0", "1"), ("1", "2"), ("2", "3")])
print(df.get_values())
try:
    print(df.ix[("0", "1")])
except:
    print("yes, accessing .ix with tuple does not work")
print(df.xs(("0", "1")))
