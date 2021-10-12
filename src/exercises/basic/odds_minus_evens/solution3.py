def my_map(x):
    if x % 2 == 0:
        return -x
    return x


def odds_minus_evens(l):
    """ Returns the sum of odd numbers in the list minus the sum of evns """
    return sum(map(my_map, l))


print(odds_minus_evens(range(1, 6)))
