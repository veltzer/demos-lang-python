"""
Show the size of a data structure in python

We can see that the size of the first array is about 4Mb
which makes sense if each int is 4 bytes.
"""

import sys

l = [x for x in range(1000000)]
print('getsizeof is [{0}]'.format(sys.getsizeof(l)))
