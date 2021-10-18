"""
This example shows how to create a read only dictionary
"""


class ReadOnlyException(Exception):
    pass


class RoDict:
    def __init__(self):
        self.d = {}
        self.ro = False

    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, val):
        if self.ro:
            raise ReadOnlyException()
        self.d[key] = val


d = RoDict()
d['a'] = 'b'
d['c'] = 'd'
print(d['a'])
d['a'] = 'e'
d.ro = True
try:
    d['a'] = 'u'
except ReadOnlyException:
    print("yes, got exception. Dictionary is read only")
