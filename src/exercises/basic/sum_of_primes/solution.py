#!/usr/bin/env python3

import math

def is_prime(n):
    for j in range(2,int(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return True 

sum = 0
for i in range(2,1000):
    if is_prime(i):
        sum += i
print(f"sum is {sum}")
