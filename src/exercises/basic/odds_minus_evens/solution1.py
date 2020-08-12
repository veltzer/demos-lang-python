import functools


def my_func(x, y):
    if y % 2 == 0:
        return x - y
    else:
        return x + y


def odds_minus_evens(l):
    result = functools.reduce(my_func, l)
    if l[0] % 2 == 0:
        result -= 2 * l[0]
    return result


print(odds_minus_evens(range(2, 6)))
