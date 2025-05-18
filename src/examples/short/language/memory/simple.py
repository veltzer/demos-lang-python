""" simple.py """


import sys

# big_l = [0,1,2,3,4,5,6,7,8,9, [0] * 10000]
big_l = [1] * 10000

print(f"big_l takes up {sys.getsizeof(big_l)} bytes")

# sys.exit(1)
# lets add up all the elements:

size = 0
size += sys.getsizeof(big_l)
for x in big_l:
    size += sys.getsizeof(x)
print(f"accumulated size of big_l is {size} bytes")
