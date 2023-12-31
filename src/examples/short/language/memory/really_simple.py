from sys import getsizeof

long_list = [0,1,2,3,4,5,6,7,8,9, [0] * 1000000]

print(f"long_list takes up {getsizeof(long_list)} bytes")
