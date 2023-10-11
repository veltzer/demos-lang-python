"""
A demo of how to use the `get_close_matches` method of the standard `difflib` library.

References:
- https://docs.python.org/3/library/difflib.html
"""

from difflib import get_close_matches

result = get_close_matches(
    word="appel",
    possibilities=["ape", "apple", "peach", "puppy"],
    n=1,
    cutoff=0.8,
)
print(result)
