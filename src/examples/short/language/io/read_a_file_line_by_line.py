"""
This example shows how to read a file line by line.
This is especially good for very large files.

References:
- http://stackoverflow.com/questions/8009882/how-to-read-large-file-line-by-line-in-python
"""

count = 0
with open("/etc/passwd") as f:
    for line in f:
        count += 1
print(count)
