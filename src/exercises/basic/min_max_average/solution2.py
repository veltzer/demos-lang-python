"""
Solution2
"""


def my_min(my_list):
    current_min = my_list[0]
    for x in my_list:
        current_min = min(current_min, x)
    return current_min


def my_max(my_list):
    current_max = my_list[0]
    for x in my_list:
        current_max = max(current_max, x)
    return current_max


def my_sum(my_list):
    current_sum = 0
    for x in my_list:
        current_sum += x
    return current_sum


def min_max_avg(my_list):
    return my_min(my_list), my_max(my_list), float(my_sum(my_list)) / len(my_list)


print(min_max_avg(range(0, 100000)))
