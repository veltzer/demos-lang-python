"""
A simple example of how to write a TSV file using the 'tsv' module
"""

import tsv

with open("/tmp/file.tsv", "w") as f:
    writer = tsv.TsvWriter(f)
    writer.comment("This is a comment")
    writer.line("Column 1", "Column 2", 12345)
    writer.list_line(["Column 1", "Column 2"] + list(range(10)))
    writer.close()
