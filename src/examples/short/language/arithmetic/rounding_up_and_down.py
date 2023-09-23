"""
This example shows how to round up and down

NOTES:
- in python2 the "ceil" and "floor" class methods of math return float types
and not ints as in python3. python3 is saner.

References:
- http://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
"""

import math

x = math.ceil(6.25)
print(type(x), x)

x = math.floor(6.75)
print(type(x), x)
