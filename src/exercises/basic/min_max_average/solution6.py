import functools


def single_min_max_sum(x, y):
    if x < y:
        min_value = x
        max_value = y
    else:
        min_value = y
        max_value = x
    sum_value = x + y
    return [min_value, max_value, sum_value]


def min_max_avg(number_list):
    tup = functools.reduce(single_min_max_sum, number_list)
    return tup[0], tup[1], tup[2] / len(number_list)


print(min_max_avg(range(0, 100000)))
