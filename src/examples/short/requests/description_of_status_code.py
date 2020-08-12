"""
This example shows how to get the description of various
http status codes.

References:
- https://stackoverflow.com/questions/24718557/get-the-description-of-a-status-code-in-python-requests
"""

import requests

def get_http_status_string(code: int):
    """
    This function returns a description of an HTTP status code (404 - not found etc).
    Unfortunately, the requests module does not provide a clean API for this so
    we must access a protected member (underscore member) of 'requests.status_code'.
    See:
    https://stackoverflow.com/questions/24718557/get-the-description-of-a-status-code-in-python-requests
    :param code:
    :return:
    """
    # noinspection PyProtectedMember
    return "http code [{}], [{}]".format(code, requests.status_codes._codes[code][0])

url = 'http://www.google.com/doesntexist'
r = requests.get(url)
print(get_http_status_string(r.status_code))
