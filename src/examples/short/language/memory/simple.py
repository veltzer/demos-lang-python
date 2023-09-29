

from sys import getsizeof as gs

big_l = [0,1,2,3,4,5,6,7,8,9, [0] * 10000]

print(f"big_l takes up {gs(big_l)} bytes")

# lets add up all the elements:

size = 0
size += gs(big_l)
for x in big_l:
    size += gs(x)
print(f"accumulated size of big_l is {size} bytes")
