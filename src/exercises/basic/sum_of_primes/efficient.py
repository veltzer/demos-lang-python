"""
Efficient
"""

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
            # print(primes_found)  # noqa: ERA001  teaching: kept in the comment for the reader
            # print(len(primes_found))  # noqa: ERA001  teaching: kept in the comment for the reader
            # print(i)  # noqa: ERA001  teaching: kept in the comment for the reader
    return primes_found


print(sum(collect_all_primes(1000000)))
