"""
This is an example of how to reassemble a url after breaking it up

The parts of the ParseResult object are:
    scheme
    netloc
    path
    params
    query
    fragment

The problem with this method is that the "_replace" method is considered
private and development environments and linters will give you hell about that.
"""


import urllib.parse

url = "https://www.wish.com/search/living%20room#default"
o = urllib.parse.urlparse(url)
print(dir(o))
r = o._replace(netloc="foo.com", path="", params="", query="", fragment="")
print(r.geturl())
