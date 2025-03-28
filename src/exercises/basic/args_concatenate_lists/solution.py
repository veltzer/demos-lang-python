"""
Solution
"""


def catenate_lists(*args):
    r = []
    for e in args:
        r.extend(e)
    return r


def catenate_lists_2(*args):
    r = []
    for e in args:
        for x in e:
            r.append(x)
    return r


l1 = [1,2,3]
l2 = [4,5,6,7]
l3 = [8,9,10]

r1 = catenate_lists(l1, l2, l3)
r2 = catenate_lists(l1, l3)

print(r1)
print(r2)
