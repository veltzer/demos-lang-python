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
            # If you have chunk encoded response filter out empty chunks
            # and set chunk_size parameter to None.
            stream.writelines(request.iter_content(chunk_size=chunk_size))


download_file(
    url="http://www.google.com",
    filename="/tmp/downloaded",
)
