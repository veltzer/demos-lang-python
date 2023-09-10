import math


def is_prime(x):
    if x == 1:
        return True
    for j in range(2, int(math.floor(math.sqrt(x))) + 1):
        if x % j == 0:
            return False
    return True


my_sum = 0
for i in range(1000000):
    if is_prime(i):
        my_sum += i
print(my_sum)
