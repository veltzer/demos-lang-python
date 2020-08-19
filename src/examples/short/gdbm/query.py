"""
This is an example of how to query the values in a gdbm file.
"""

import dbm.gnu
import os.path

filename = "/tmp/test.gdbm"

if os.path.isfile(filename):
    os.unlink(filename)

# lets put in some data
d = dbm.gnu.open(filename, 'n')
d["one"] = "yes!"
d.close()

# lets open for read
# the 'r' in the next line means open for read only
d = dbm.gnu.open(filename, 'r')

print('one in db', 'one' in d)
print('two in db', 'two' in d)

# lets query a key which isn't there
try:
    print(d["one"])
except KeyError as e:
    print("yes!, got KeyError")

d.close()
