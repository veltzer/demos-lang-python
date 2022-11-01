"""
This is an example that gets an enviroment variable and verifies that it exists

References:
- https://stackoverflow.com/questions/40697845/what-is-a-good-practice-to-check-if-an-environmental-variable-exists-or-not
- https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
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
