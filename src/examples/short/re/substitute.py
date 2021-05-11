"""
Example of how to substitute parts of a string using regular expressions.
"""

import re

print(re.sub(r'abc', 'z', 'abcdefghijkabcde'))
