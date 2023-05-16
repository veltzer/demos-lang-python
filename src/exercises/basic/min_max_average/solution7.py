"""
this solution is the "varargs" type. You can call the min_max_avg function in any
of the following ways:
(my_max,my_min,my_avg)=min_max_avg(1,2,3)
(my_max,my_min,my_avg)=min_max_avg(1,2,3,4,5,6)
(my_max,my_min,my_avg)=min_max_avg(*range(100000))
"""


def min_max_avg(*num_list):
    """return a tuple containing the maximnum_list, minimum and avrage of the given num_listbrs"""
    return min(num_list), max(num_list), sum(num_list) / len(num_list)


# print(min_max_avg(6,7,2,3,4))
print(min_max_avg(*range(100000)))
