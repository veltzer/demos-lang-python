"""
Show the size of a data structure in python

We can see that the size of the first array is about 4Mb
which makes sense if each int is 4 bytes.
"""

import sys

my_list = list(range(1000000))
print(f"getsizeof is [{sys.getsizeof(my_list)}]")
