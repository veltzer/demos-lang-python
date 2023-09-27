import math

# primes holds integers as keys and booleans as values
primes = {}

def cache(func):
    def new_is_prime(n):
        if n in primes:
            return primes[n]
        b = func(n)
        primes[n] = b
        return b
    return new_is_prime

@cache
def is_prime(n):
    print("in called")
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True


print(is_prime(7))
print(is_prime(7))

# test 'is_prime'
# for i in range(100):
#     if is_prime(i):
#         print(i)
