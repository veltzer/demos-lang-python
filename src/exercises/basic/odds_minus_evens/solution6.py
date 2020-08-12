def odds_minus_evens(l):
    """ Returns the sum of odd numbers in the list minus the sum of evns """
    return sum(filter(lambda x: x % 2 != 0, l)) - sum(filter(lambda x: x % 2 == 0, l))
