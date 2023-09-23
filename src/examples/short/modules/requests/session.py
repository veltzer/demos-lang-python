"""
This example shows how to use a session. You will probaly
want a session whenever you do many requests in a row.

References:
- https://requests.readthedocs.io/en/latest/user/advanced/
"""

import requests

session = requests.Session()
response = session.get("https://www.google.com", timeout=5)
print(len(response.content))
