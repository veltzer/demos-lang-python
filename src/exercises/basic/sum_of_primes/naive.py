import math

def is_prime(x):
    if x==1:
        return True
    for i in range(2,int(math.floor(math.sqrt(x)))+1):
        if x%i==0:
            return False
    return True

sum = 0
for i in range(1000000):
    if is_prime(i):
        sum += i
print(sum)
