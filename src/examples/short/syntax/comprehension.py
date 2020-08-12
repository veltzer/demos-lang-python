"""
Exapmles of various types of comprehensions.
"""

# multiplication table as comprehenshion
l = [x * y for x in range(10) for y in range(10)]
print(l)

# same code as above without comprehensions
new_list = []
for x in range(10):
    for y in range(10):
        new_list.append(x * y)
print(new_list)

tup_list = []
for x in range(10):
    for y in range(10):
        tup_list.append((x, y))
print(map(lambda t: t[0] * t[1], tup_list))

# sets
print({x * 2 for x in range(10)})
print({2, 3, 4})

# dictionaries
print({2: 3, 4: 5})
print({x: x ** 2 for x in range(10)})

d = {'one': 'onev', 'two': 'twov'}
print(dict((y, x) for x, y in d.items()))
