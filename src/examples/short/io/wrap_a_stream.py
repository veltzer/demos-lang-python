"""
This example will show how to wrap one io object with another.

References:
- http://stackoverflow.com/questions/34447623/wrap-an-open-stream-with-io-textiowrapper
"""

import io
import itertools

filename = "/etc/passwd"

# default mode of open is "rt"
with open(filename, "rb") as file_handle1:
    for line in itertools.islice(file_handle1, 5):
        print(line)

with open(filename, "rb") as file_handle2:
    wrapped = io.TextIOWrapper(file_handle2)
    for line2 in itertools.islice(wrapped, 5):
        print(line2, end="")
