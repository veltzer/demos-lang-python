"""
This example shows how to handle the HTTP return codes
in order to print nice error messages.

Remember that you dont need to do that since requests has
r.raise_for_status() which raises nice exceptions...
This is only needed in older versions of python which did not have
that method.
"""

import requests


def get_http_status_string(code: int) -> str:
    """
    This function returns a description of an HTTP status code (404 - not found etc).
    The requests module has no direct API for this so we look the code up
    in the public "requests.codes" table.
    See:
    https://stackoverflow.com/questions/24718557/get-the-description-of-a-status-code-in-python-requests
    :param code:
    :return:
    """
    name = next(n for n, c in vars(requests.codes).items() if c == code)
    return f"http code [{code}], [{name}]"


url = "http://google.com"
r = requests.get(url, timeout=5)
assert r.status_code == 200, get_http_status_string(r.status_code)
response = r.content.decode()
print(len(response))
