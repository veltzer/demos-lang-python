"""
A simple example of how to get or set environment variables from python
"""

import os

print(os.environ['USER'])
if 'HOSTNAME' in os.environ:
    print(os.environ['HOSTNAME'])
else:
    print(
        'you dont have a HOSTNAME in your environment, it is probably just a shell variable')

# lets delete an environment variable
del os.environ['USER']
assert 'USER' not in os.environ

for k, v in os.environ.items():
    print(k, v)
