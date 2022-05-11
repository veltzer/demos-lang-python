"""
This example why you should prefer builtin functional approaches or numpy
approaches to traditional range for loops...

References:
- https://towardsdatascience.com/a-super-fast-way-to-loop-in-python-6e58ba377a00
"""

import timeit
import functools
import numpy as np


def do_sum_range():
    total_sum = 0
    for i in range(100000000):
        total_sum += i
    print(f'Sum: {total_sum}')


def do_sum_functional():
    total_sum = sum(range(100000000))
    print(f'Sum: {total_sum}')


def do_sum_numpy():
    total_sum = np.sum(np.arange(100000000))
    print(f'Sum: {total_sum}')


def do_stats_for(random_scores):
    count_failed = 0
    sum_failed = 0
    for score in random_scores:
        if score < 70:
            sum_failed += score
            count_failed += 1
    mean = sum_failed / count_failed
    print(f"mean is {mean}")


def do_stats_numpy(random_scores):
    mean = (random_scores[random_scores < 70]).mean()
    print(f"mean is {mean}")


print(timeit.timeit(do_sum_range, number=1))
print(timeit.timeit(do_sum_functional, number=1))
print(timeit.timeit(do_sum_numpy, number=1))
random_scs = np.random.randint(1, 100, size=100000010)
print(timeit.timeit(functools.partial(do_stats_for, random_scs), number=1))
print(timeit.timeit(functools.partial(do_stats_numpy, random_scs), number=1))
