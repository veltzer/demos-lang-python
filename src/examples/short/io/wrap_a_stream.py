"""
This example will show how to wrap one io object with another.

References:
- http://stackoverflow.com/questions/34447623/wrap-an-open-stream-with-io-textiowrapper
"""

import io
import itertools
from io import BufferedIOBase

filename = "/etc/passwd"

# default mode of open is "rt"
with open(filename, "rb") as file_handle:
    for line in itertools.islice(file_handle, 5):
        print(line)

with open(filename, "rb") as file_handle:  # type: BufferedIOBase
    wrapped = io.TextIOWrapper(file_handle)
    for line in itertools.islice(wrapped, 5):
        print(line, end='')
