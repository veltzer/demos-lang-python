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
    url_to_test = "http://nikuda.co.il/"
else:
    url_to_test = sys.argv[1]

print(f"testing url {url_to_test}")
url_of_wpt_run = "http://localhost/runtest.php"
# url_of_wpt_run = "https://www.webpagetest.org/runtest.php"
r = requests.get(url_of_wpt_run, params={
    'url': url_to_test,
    'f': 'json',
    'location': 'Test',
    # 'runs': 1,
    # 'fvonly': 1,
    # 'private': 1,
    # 'timeline': 1,
})
assert r.status_code == 200, get_http_status_string(r.status_code)
response_obj = r.json()
# print(json.dumps(response_obj, indent=4, sort_keys=True))
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
    job_status_code = int(response_obj["statusCode"])
    if job_status_code == 200:
        over = True
        break
    # print(json.dumps(response_obj, indent=4, sort_keys=True))
    time.sleep(1)

print(f"getting results from url {jsonUrl}")
r = requests.get(jsonUrl)
assert r.status_code == 200, get_http_status_string(r.status_code)
response_obj = r.json()
with open("/tmp/results.json", "w") as f:
    json.dump(
        obj=response_obj,
        fp=f,
        indent=4,
        sort_keys=True,
    )
