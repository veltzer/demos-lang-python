"""
this is an example of implementing the python builtin "map"
function in python.

Obviously you should not use this approach and it is presented
for pedagogic purposes only. Pythons own "map" is written in C
and performs much better.
"""


def my_map(f, seq):
    y = []
    for x in seq:
        y.append(f(x))
    return y


print(my_map(lambda x: x * x, range(10)))
