import timeit
import random

check_from = 37
check_to = 51
num_checks = 1000000

random_list = [random.randrange(0, 100) for _i in range(0, num_checks)]


def func_naive() -> int:
    count = 0
    for i in random_list:
        # noinspection PyChainedComparisons
        if i >= check_from and i < check_to:
            count += 1
    return count


def func_concise() -> int:
    count = 0
    for i in random_list:
        if check_from <= i < check_to:
            count += 1
    return count


def func_range() -> int:
    count = 0
    for i in random_list:
        if i in range(check_from, check_to):
            count += 1
    return count


print("naive: {}".format(timeit.timeit(func_naive, number=1)))
print("concise: {}".format(timeit.timeit(func_concise, number=1)))
print("range: {}".format(timeit.timeit(func_range, number=1)))
