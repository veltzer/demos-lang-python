"""
Example of sorting with python using the key parameter

The "list.sort" function is a core python function.
"""


def compare(item):
    return item[1]


m = {"mark": 10, "yossi": 3, "doron": 67}
my_list = list(m.items())
my_list.sort(key=compare)

print(my_list)
