"""
This is an exmple of how to parse a query string using the "urllib.parse"
library in python3
"""

import urllib.parse

r = urllib.parse.parse_qs("sk=Crystal-Rush&so=0&ss=latest")
print(r)
