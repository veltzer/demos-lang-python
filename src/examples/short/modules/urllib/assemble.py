"""
This is an example of how to assemble a path.

Assemble by the following order:
    scheme
    netloc
    path
    query
    fragment

"""


import urllib.parse

# must have 5 elements of the order above
p = ["https", "wish.com", "hello", "f=2", "frag"]
print(urllib.parse.urlunsplit(p))
