import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


# test 'is_prime'
# for i in range(100):
#     if is_prime(i):
#         print(i)
