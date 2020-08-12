import functools


def my_min(x, y):
    if x < y:
        return x
    else:
        return y


def my_max(x, y):
    if x < y:
        return y
    else:
        return x


def my_sum(x, y):
    return x + y


def min_max_avg(list):
    rmin = functools.reduce(my_min, list)
    rmax = functools.reduce(my_max, list)
    rsum = functools.reduce(my_sum, list)
    return rmin, rmax, rsum / len(list)


print(min_max_avg(range(0, 100)))
