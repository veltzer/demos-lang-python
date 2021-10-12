"""
This is an example of how to insert a large value into a gdbm file.

Notes:
- the conclusion is that you can put as large a key or value in a gdbm database
as you want.
"""

import dbm.gnu
import os.path

# the 'c' in the next row means open rw and create if it doesn't exist
filename = "/tmp/test.gdbm"
large_text_filename = "/var/log/auth.log"

if os.path.isfile(filename):
    os.unlink(filename)

large_text = open(large_text_filename).read()

# n means create a new database and open for reading and writing
d = dbm.gnu.open(filename, 'n')
d['large'] = large_text
d[large_text] = 'is this possible'
d.close()

# lets open the file
d = dbm.gnu.open(filename)
value = d['large'].decode()
assert value == large_text
value = d[large_text].decode()
assert value == 'is this possible'
d.close()
