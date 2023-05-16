"""
This example shows how to do incremental packing and unpacking
using the "struct" module.

Notes:
- pack

References:
- https://docs.python.org/3/library/struct.html
"""

import ctypes
import struct


class Encoder:
    def __init__(self, size):
        super().__init__()
        self.dict = {
            "i": struct.Struct("i").size,
        }
        self.size = size
        self.buffer = ctypes.create_string_buffer(size)
        self.pos = 0

    def get_bytes(self):
        """ return all the bytes collected """
        return self.buffer[:self.pos]


# pack two numbers
v1_in = 2
v2_in = 3
b = ctypes.create_string_buffer(50)
print(ctypes.sizeof(b))
print(f"len(b) is [{len(b)}]")
print(struct.Struct("i").size)
struct.pack_into("i", b, 0, v1_in)
struct.pack_into("i", b, 4, v2_in)
t = b[:8]
assert isinstance(t, bytes)
