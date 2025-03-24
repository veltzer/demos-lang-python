"""
Solution11
"""

def max_min_avg(*num):
    """return a tuple containing the maximnum, minimum and avrage of the given numbers"""
    return max(num), min(num), sum(num) / len(num)
