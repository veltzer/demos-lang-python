"""
our_code.py
"""

import requests


def our_function_to_test():
    url = "http://localhost:8080"
    r = requests.get(url, timeout=5)
    r.raise_for_status()
