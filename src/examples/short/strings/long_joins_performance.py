"""
This example proves that when you want to catenate many strings 'join' is
the right way to go.
"""

import timeit


def func1():
    s = names[0]
    for name in names[1:]:
        s += ', ' + name
    return s


func1.name = 'plus'


def func2():
    return ','.join(names)


func2.name = 'join'

names = []
for i in range(1000000):
    names.append('name' + str(i))

functions = [
    func1,
    func2,
]

number = 100
results = [(timeit.timeit(f, number=number), f.name) for f in functions]
sorted_results = sorted(results, key=lambda tup: tup[0])
for r in sorted_results:
    print('{0:.4f}: {1}'.format(r[0], r[1]))
