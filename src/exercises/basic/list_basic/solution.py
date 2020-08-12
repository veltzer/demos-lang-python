def mysum(lst):
    """A function receiving a list of integers and returning the sum
    of the integers on the list"""
    s = 0
    for x in lst:
        s += x
    return s


print('the sum is ', mysum([1, 2, 3, 4, 5]))
