"""
This example lists the various ways to get the current user name in python.

References:
- http://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python
"""

import getpass
import os
import pwd

print(getpass.getuser())
print(os.getlogin())
print(pwd.getpwuid(os.getuid())[0])
