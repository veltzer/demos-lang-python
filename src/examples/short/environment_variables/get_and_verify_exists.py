"""
This is an example that gets an enviroment variable and verifies that it exists
"""

import os


def get_strict(name: str):
    assert name in os.environ, f"missing environment variable [{name}]"
    return os.getenv(name)

print(get_strict("HOME"))
