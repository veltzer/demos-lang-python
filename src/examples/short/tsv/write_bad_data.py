"""
This example shows that you can write bad data into TSV files
using the "tsv" module
"""

import tsv

with open("/tmp/file.tsv", "w") as f:
    writer = tsv.TsvWriter(f)
    writer.line("\t\t\t", "Column 2", 12345)
    writer.close()
