"""
Solution10
"""

def max_min_avg(*num):
    """Return a tuple containing the maximum, minimum and average
    of the given numbers"""
    return max(num), min(num), sum(num) / len(num)


print(max_min_avg(3, 4, 5))


def max_min_avg_2(lst):
    """Return a tuple containing the maximum, minimum and average
    of the given numbers"""
    return max(lst), min(lst), sum(lst) / len(lst)


print(max_min_avg_2([3, 4, 5]))
print(max_min_avg_2((3, 4, 5)))


def max_min_avg_3(seq):
    mysum = 0
    mymin = None
    mymax = None
    for v in seq:
        if mymin is None or v < mymin:
            mymin = v
        if mymax is None or v > mymax:
            mymax = v
        mysum += v
    return mymax, mymin, mysum / len(seq)


print(max_min_avg_3([3, 4, 5]))
