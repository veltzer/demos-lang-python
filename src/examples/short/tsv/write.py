"""
A simple example of how to write a TSV file using the "tsv" module
"""

import tsv

with open("/tmp/file.tsv", "w") as f:
    writer = tsv.TsvWriter(f)
    writer.comment("This is a comment")
    writer.line("Column 1", "Column 2", 12345)
    my_list = [
        "Column 1",
        "Column 2",
    ]
    ten = [str(i) for i in range(10)]
    my_list.extend(ten)
    writer.list_line(my_list)
    writer.close()
