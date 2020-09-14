"""
An example of passing parameters to an HTTP GET request.

References:
- https://stackoverflow.com/questions/6386308/http-requests-and-json-parsing-in-python
"""

import requests

url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false',
)

resp = requests.get(url=url, params=params)
assert resp.status_code == 200, resp.status_code
data = resp.json() # Check the JSON Response Content documentation below
print(data)
