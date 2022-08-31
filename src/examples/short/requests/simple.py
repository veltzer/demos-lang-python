"""
A basic example showing the use of the requests module

References:
- http://docs.python-requests.org/en/master
- http://docs.python-guide.org/en/latest/scenarios/scrape
"""

import requests

url = 'http://www.google.com'
r = requests.get(url, timeout=5)
# this checks if the return status is 200 and is similar to:
# assert r.status_code == 200
r.raise_for_status()
print(len(r.content))
# print(r.content)
