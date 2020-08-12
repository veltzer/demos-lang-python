"""
This example shows that you can write bad data into TSV files
using the 'tsv' module
"""

import tsv

writer = tsv.TsvWriter(open("/tmp/file.tsv", "w"))

writer.line("\t\t\t", "Column 2", 12345)
writer.close()
