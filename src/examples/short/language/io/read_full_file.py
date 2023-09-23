"""
This example shows how to read the full content of a file in python

In order to read the entire file you must open it in binary mode.

References:
- http://stackoverflow.com/questions/7409780/reading-entire-file-in-python
"""

source_file = "/etc/passwd"

with open(source_file) as file_handle:
    content = file_handle.read()
print(content, end="")
