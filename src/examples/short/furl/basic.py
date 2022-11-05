"""
A basic example of how to use the furl module
This is an example of how you take a url, break it down, add user and password
to it and get everything back together.

References:
- https://sadique.io/blog/2017/09/26/python-url-manipulation-revisited/
"""

from furl import furl

url = furl('http://example.com')
print(url)
url.password = "password"
url.username = "user"
print(url)
