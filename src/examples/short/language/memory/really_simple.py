from sys import getsizeof

l = [0,1,2,3,4,5,6,7,8,9, [0]*1000000]

print(f"l takes up {getsizeof(l)} bytes")
