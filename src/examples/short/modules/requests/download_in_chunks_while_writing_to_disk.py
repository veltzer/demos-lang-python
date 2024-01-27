"""
This example shows how to use the "requrest" python module to download
a large file in small chunks and save it to disk.

References:
- https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
"""

import requests


def download_file(url: str, filename: str, chunk_size=8192):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True, timeout=5) as request:
        request.raise_for_status()
        with open(filename, "wb") as stream:
            for chunk in request.iter_content(chunk_size=chunk_size):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                stream.write(chunk)


download_file(
    url="http://www.google.com",
    filename="/tmp/downloaded",
)
