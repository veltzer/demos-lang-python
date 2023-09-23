"""
Show how to convert using bitmath

References:
- https://pypi.org/project/bitmath/
"""

import bitmath


number = bitmath.Byte(100 * 1000 * 1000 * 1000)
print(dir(number))
print(number.to_GB())
