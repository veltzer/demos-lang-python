"""
This example attempts to compare ujson.loads with struct.unpack
to see which is faster.

Results:
TBD

References:
- https://docs.python.org/3/library/struct.html
"""

import struct


class DataToPack:
    def __init__(self, v1, v2, s):
        self.v1 = v1
        self.v2 = v2
        self.s = s

    def pack(self):
        return struct.pack(
            "iis",
            self.v1,
            self.v2,
            self.s,
        )

    def unpack(self, b):
        """ unpack into self """

    def __str__(self):
        return "DataToPack: {}, {}, {}".format(self.v1, self.v2, self.s)


d = DataToPack(2, 3, "hello")
print(d)
