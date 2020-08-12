"""
    this example shows that you can pass any generator/sequence to a function
    that only uses the generator/sequence API and get the right results.
    What can't you do? Use slices on generators but that is obvious.
"""


def myfunc(s):
    for i in s:
        print(i, end='')
    print()


myfunc(range(10))
myfunc(range(10))
myfunc((1, 2, 3))
myfunc([1, 2, 3])
myfunc('hello')
myfunc(range(10)[:5])
# these will not work
# print(range(10)[:5])
# myfunc(range(10)[:5])
