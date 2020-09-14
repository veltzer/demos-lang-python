import json
import sys
import time

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
    # noinspection PyProtectedMember,PyUnresolvedReferences
    return f"http code [{code}], [{requests.status_codes._codes[code][0]}]"


if len(sys.argv) == 1:
    url_to_test = "https://google.com"
else:
    url_to_test = sys.argv[1]
print(f"testing url {url_to_test}")

url_of_wpt_run = "http://localhost/runtest.php"
r = requests.get(url_of_wpt_run, params={
    'url': url_to_test,
    'f': 'json',
})
assert r.status_code == 200, get_http_status_string(r.status_code)
response_obj = r.json()
# print(json.dumps(response_obj, indent=4, sort_keys=Tru
testId = response_obj["data"]["testId"]
jsonUrl = response_obj["data"]["jsonUrl"]
print(f"testId is {testId}")
print(f"jsonUrl is {jsonUrl}")

url_of_wpt_test = "http://localhost/testStatus.php"

over = False
while not over:
    print(f"polling {url_of_wpt_test} for id {testId}...")
    r = requests.get(url_of_wpt_test, params={
        'f': 'json',
        'test': testId,
    })
    assert r.status_code == 200, get_http_status_string(r.status_code)
    response_obj = r.json()
    print(json.dumps(response_obj, indent=4, sort_keys=True))
    time.sleep(1)
