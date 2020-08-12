"""
This example shows how to create a histogram using numpy

Notes:
- histogram returns two arrays as output.
The first is as long as number of bins you requested
and has the count for each bin.
- The second is one longer and has the values associated
with each bin.

References:
- https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.histogram.html
"""

import numpy

a = [1, 2, 3, 4, 11, 16, 17, 18, 20.5]

print(numpy.histogram(a, bins=3))
