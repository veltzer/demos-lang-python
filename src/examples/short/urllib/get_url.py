"""
A basic demo of how to download urls off the web.

References:
http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
"""

import urllib.request

with urllib.request.urlopen("http://python.org") as response:
    html = response.read()
    print(html)
