"""
This example demonstrates how to use the python builtin 'struct'
module.

Notes:
- struct.pack return type is 'bytes'
- struct.unpack return type is tuple
- length of a packed buffer is exactly what you would expect it to be
from the import basic types that you are packing.

References:
- https://docs.python.org/3/library/struct.html
"""

import struct

# pack two numbers
v1_in = 2
v2_in = 3
packed = struct.pack("ih", v1_in, v2_in)
assert len(packed) == 6
assert type(packed) == bytes
v1, v2 = struct.unpack("ih", packed)
assert v1 == v1_in
assert v2 == v2_in
