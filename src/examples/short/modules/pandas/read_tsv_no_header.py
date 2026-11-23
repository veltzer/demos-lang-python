"""
This is an example of how to read a tsv file with no header.

The idea is to:
  pass header=None
  pass sep="\t",
"""

import pandas as pd

filename = "shared-samples/tsv/2_by_2.tsv"
df = pd.read_csv(
    filename,
    sep="\t",
    header=None,
)
assert df.shape == (2,2)
