import requests


"""
Test is to see if google gives a web reply to python request without
having to fake the type of web client
"""



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
    # noinspection PyProtectedMember,PyUnresolvedReferences
    return f"http code [{code}], [{requests.status_codes._codes[code][0]}]"


url= "http://google.com"
r = requests.get(url)
assert r.status_code == 200, get_http_status_string(r.status_code)
response = r.content.decode()
print(response)
