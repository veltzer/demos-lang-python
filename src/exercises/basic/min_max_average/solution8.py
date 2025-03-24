"""
Solution8
"""

def my_min(lst):
    cur_min = lst[0]
    for x in lst:
        cur_min = min(cur_min, x)
    return cur_min


def my_max(lst):
    cur_max = lst[0]
    for x in lst:
        cur_max = max(cur_max, x)
    return cur_max


def my_sum(lst):
    cur_sum = 0
    for x in lst:
        cur_sum += x
    return cur_sum


def min_max_avg(lst):
    return my_min(lst), my_max(lst), my_sum(lst) / len(lst)


print(min_max_avg(range(100000)))
