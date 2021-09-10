"""
A simple example of how to read a TSV file using the 'tsv' module
"""

import tsv

reader = tsv.TsvReader(open("data/tsv/file.tsv"))
for parts in reader:
    parts = list(parts)
    # Here parts is a list of strings, one per tab-separated column.
    # Make sure you handle not having enough fields, or not being able to
    # parse numbers where you expect them.
    print("Record with fields: {}".format(parts))
