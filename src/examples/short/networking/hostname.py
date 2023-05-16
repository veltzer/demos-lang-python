"""
This example shows the various ways to get the host name in python.

References:
http://stackoverflow.com/questions/4271740/how-can-i-use-python-to-get-the-system-hostname
"""

import os
import platform
import socket

print(socket.gethostname())
print(platform.node())
print(platform.uname()[1])
print(os.uname()[1])
print(os.getenv("HOSTNAME"))
# HOSTNAME is not always an environment variables so this may not work
print(os.getenv("HOST"))
# HOST is not always an environment variables so this may not work
print(socket.gethostbyaddr(socket.gethostname())[0])
print(socket.getfqdn())
