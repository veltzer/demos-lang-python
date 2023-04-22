"""
This is an example of how to do a weighted sample using pandas.
"""

import pandas

filename = "data_samples/2_by_2.tsv"
df = pandas.read_csv(
    filename,
    sep='\t',
    header=None,
)

weight_column_number = 1
value_column_number = 0
size_of_sample = 10

sample = df.sample(
    n=size_of_sample,
    replace=True,
    weights=df[df.columns[weight_column_number]],
)
res = sample[sample.columns[value_column_number]].value_counts()
print(res)
