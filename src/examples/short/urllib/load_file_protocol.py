"""
An example of using 'urllib' for loading files with the "file:" protocol.

References:
- ???
"""

import urllib.request

url = "file:/etc/passwd"
with urllib.request.urlopen(url) as response:
    data = response.read()
    print(data)
