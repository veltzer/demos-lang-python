"""
An example of getting the latest request of a package from github

References:
- https://stackoverflow.com/questions/60716016/how-to-get-the-latest-release-version-in-github-only-use-python-requests
"""

import requests


owner = 'veltzer'
repo = 'pyflexebs'

response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/releases/latest", timeout=5)
response.raise_for_status()
print(response.json()["name"])
