"""
This is a demo of how to use the "requests" module to download a url (possibly
a large blob) into a temporary file which gets "auto deleted" using the
standard NamedTemporaryFile tempfile context manager.

References:
- https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
"""


import shutil
import urllib.request
import tempfile
import os.path


url = "http://google.com"
filename = None
with tempfile.NamedTemporaryFile() as file_handle:
    filename = file_handle.name
    with urllib.request.urlopen(url) as fsrc:
        shutil.copyfileobj(fsrc, file_handle)
    assert os.path.isfile(filename)
assert not os.path.isfile(filename)
