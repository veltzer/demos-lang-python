"""
This example shows how to create a read only dictionary
"""

from typing import Any


class ReadOnlyError(Exception):
    pass


class RoDict:
    def __init__(self) -> None:
        self.d = {}
        self.ro = False

    def __getitem__(self, key: str):
        return self.d[key]

    def __setitem__(self, key: str, val: Any) -> None:
        if self.ro:
            raise ReadOnlyError
        self.d[key] = val


d = RoDict()
d["a"] = "b"
d["c"] = "d"
print(d["a"])
d["a"] = "e"
d.ro = True
try:
    d["a"] = "u"
except ReadOnlyError:
    print("yes, got exception. Dictionary is read only")
