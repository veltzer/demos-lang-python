def odds_minus_evens(l):
    """ Returns the sum of odd numbers in the list minus the sum of evns """
    sum = 0
    for x in l:
        if x % 2 == 0:
            sum -= x
        else:
            sum += x
    return sum


print(odds_minus_evens(range(10)))
