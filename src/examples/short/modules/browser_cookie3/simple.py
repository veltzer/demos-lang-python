"""
This is an example of how to extract a cookie for a specific site using `browser_cookie3`
"""


import browser_cookie3

cookies = browser_cookie3.chrome()

for c in cookies:
    if c.domain == ".goodreads.com" and c.name == "session-token":
        print(f"{c.domain} {c.name} {c.value}")
