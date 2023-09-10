import math


def collect_all_primes(num):
    primes_found = []
    for i in range(2,num):
        for p in primes_found:
            if i % p == 0:
                break
            if p > int(math.sqrt(i)) + 1:
                primes_found.append(i)
                break
        else:
            primes_found.append(i)
            # print(primes_found)
            # print(len(primes_found))
            # print(i)
    return primes_found


print(sum(collect_all_primes(1000000)))
