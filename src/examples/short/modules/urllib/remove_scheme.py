"""
This is an exmample of how to remove the scheme element from a url
using the urllib python built-in module.

References:
- https://stackoverflow.com/questions/21687408/how-to-remove-scheme-from-url-in-python
"""

from urllib.parse import urlparse


def strip_scheme(url: str) -> str:
    schemaless = urlparse(url)._replace(scheme="").geturl()
    return schemaless[2:]


print(strip_scheme("https://google.com"))
