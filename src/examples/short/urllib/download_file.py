"""
This is a simple example of how to download a file using the 'urllib' module.


References:
- https://stackoverflow.com/questions/22676/how-to-download-a-file-over-http
"""


import urllib.request


urllib.request.urlretrieve("http://google.com", "/tmp/google.html")
