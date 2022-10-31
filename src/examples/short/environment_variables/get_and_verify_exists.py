"""
This is an example that gets an enviroment variable and verifies that it exists
"""

import os


def get_strict(name: str):
    """
    this function gives you the value of an environment variable and fails
    if it doesnt exist
    """
    assert name in os.environ, f"missing environment variable [{name}]"
    return os.getenv(name)

print(get_strict("HOME"))
