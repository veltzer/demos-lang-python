""" by_comprehension.py """

g = (x ** 2 for x in range(6))

"""
this is same as:
def g():
    for x in range(6):
        yield x**2
"""
print(g)
for x in g:
    print(x)
