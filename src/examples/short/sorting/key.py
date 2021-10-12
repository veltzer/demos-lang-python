"""
This is an example of how to sort lists in python
using the 'key' function.

Note: in python2 you could sort lists usnig the 'cmp' function.
This no longer works and was removed in python3 (see Hettinger for reasons why...).
"""


def my_tup_reverse(t1, t2):
    if (t1[1], t1[0]) < (t2[1], t2[0]):
        return -1
    if (t1[1], t1[0]) > (t2[1], t2[0]):
        return 1
    if (t1[1], t1[0]) == (t2[1], t2[0]):
        return 0


def my_reverse(t1, t2):
    if t2 < t1:
        return -1
    if t2 > t1:
        return 1
    if t2 == t1:
        return 0


def my_second_cor_key(t):
    return t[1]


# this is a WRONG default function since it does not take into accout both co-ordinates
def the_default_function_wrong(t):
    return t[0]


# def the_default_function(t):
#    return t

# def the_default_function(t):
#    return t[0], t[1]

def the_default_function(t):
    return t[0] * 1000 + t[1]


def by_y_x(t):
    return t[1], t[0]


my_list = [(1, 7), (2, 5), (0, 0), (3, 8), (1, 8), (2, 8), (3, 2)]
# lets see how regular sort works...(prefers first co-ordinate to the second)
print("sorted by default\n", sorted(my_list))
# lets try to emulate the default behaviour of sorted with our own function...
print("sorted with only first co-ordinate\n", sorted(my_list, key=the_default_function_wrong))
# better way to emulate the default behaviour...
print("sorted with identity function\n", sorted(my_list, key=the_default_function))
# lets see how use the key function to sort by the second co-ordinate
print("sorted by second co-ordinate\n", sorted(my_list, key=my_second_cor_key))
# lets see how use the key function
print("sorted first by the second co-ordinate and then by the first\n", sorted(my_list, key=by_y_x))

# These examples no longer work in python3 !!!!

# lets see how reverse works... (no longer works)
# print(sorted(my_list, cmp=my_reverse))
# lets see how second tuple co-ordinate sort works... (no longer works)
# print(sorted(my_list, cmp=my_tup_reverse))
