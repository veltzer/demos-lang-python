"""
This is an example exploring how much does namespace lookup cost.

Solution: cache your globals
"""

import timeit

repetitions = 10
limit = 10000000
global_var = 5
global_var_2 = 7


def regular_func():
    current_sum = 0
    for _ in range(limit):
        current_sum += global_var * global_var_2
    return current_sum


def caching_func():
    current_sum = 0
    local = global_var
    local_2 = global_var_2
    for _ in range(limit):
        current_sum += local * local_2
    return current_sum


print(f"regular_func {timeit.timeit(regular_func, number=repetitions):.04f}")
print(f"caching_func {timeit.timeit(caching_func, number=repetitions):.04f}")
