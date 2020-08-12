"""
A basic example showing the use of the requests module

References:
- http://docs.python-requests.org/en/master
- http://docs.python-guide.org/en/latest/scenarios/scrape
"""

import requests

url = 'http://www.google.com'
r = requests.get(url)
assert r.status_code == 200
print(r.content)
