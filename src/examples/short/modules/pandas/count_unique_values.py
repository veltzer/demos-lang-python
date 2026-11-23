"""
This example shows how to count unique values with pandas.

References:
- https://stackoverflow.com/questions/38309729/count-unique-values-with-pandas
"""

import pandas as pd

filename = "shared-samples/tsv/3_by_2.tsv"
df = pd.read_csv(
    filename,
    sep="\t",
    header=None,
)

assert df[1].nunique() == 3
