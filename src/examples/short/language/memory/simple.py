

from sys import getsizeof as gs

l = [0,1,2,3,4,5,6,7,8,9, [0]*10000]

print(f"l takes up {gs(l)} bytes")

# lets add up all the elements:

size = 0
size += gs(l)
for x in l:
    size += gs(x)
print(f"accumulated size of l is {size} bytes")
