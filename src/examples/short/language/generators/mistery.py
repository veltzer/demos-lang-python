"""
A mistery from my brother

What will the program print and why?
"""


def mistery(x):
    return list(range(x))
    yield x


a_5 = mistery(5)
print(sum(a_5))
