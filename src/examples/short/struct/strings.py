"""
This example encodes a string using the 'struct' module.

References:
- https://docs.python.org/3/library/struct.html
"""

import struct

s_in = "my string".encode()
packed = struct.pack("s", s_in)
s_out = struct.unpack("s", packed)
assert s_out == s_in
