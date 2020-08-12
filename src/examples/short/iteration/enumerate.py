"""
This example shows how to use the 'enumerate' iterator.

Notes:
- enumerate is supposed to be efficient both in python2.7
and in python3 although I haven't checked that.
- the two code samples below do the same but the second
is more beautiful.
"""

l = ['a', 'b', 'c']

# the non pythonic way to do this
for i in range(len(l)):
    print(i, l[i])

# the pythonic way to do this
for i, c in enumerate(l):
    print(i, c)

# our own 'enumerate'
def simple_enumerate(l):
    i = 0
    for c in l:
        yield i, c
        i += 1

# now let's use our own enumerator
for i, c in simple_enumerate(l):
    print(i, c)
