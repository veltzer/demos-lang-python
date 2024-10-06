"""
This example shows how to count unique values with pandas.

References:
- https://stackoverflow.com/questions/38309729/count-unique-values-with-pandas
"""

import pandas

filename = "data_samples/3_by_2.tsv"
df = pandas.read_csv(
    filename,
    sep="\t",
    header=None,
)

assert df[1].nunique() == 3
