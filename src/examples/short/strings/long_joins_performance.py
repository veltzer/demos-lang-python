"""
This example proves that when you want to catenate many strings "join" is
the right way to go.
"""

import timeit


function_names = {}


def func1():
    s = names[0]
    for name in names[1:]:
        s += ", " + name
    return s


function_names[func1] = "plus"


def func2():
    return ",".join(names)


function_names[func2] = "join"

names = []
for i in range(1000000):
    names.append("name" + str(i))

functions = [
    func1,
    func2,
]

number = 100
results = [(timeit.timeit(f, number=number), function_names[f]) for f in functions]
sorted_results = sorted(results, key=lambda tup: tup[0])
for r in sorted_results:
    print(f"{r[0]:.4f}: {r[1]}")
