"""
This is a basic example of how to parse urls
"""

import sys
import urllib.parse

url = "https://www.wish.com/search/living%20room#default"
o = urllib.parse.urlparse(url)
qs = urllib.parse.parse_qs(o.query)
path = o.path
start = "/search/"
if not path.startswith(start):
    print("fail")
    sys.exit(1)
path = path[len(start):]
print(urllib.parse.unquote(path))
