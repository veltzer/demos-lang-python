"""
Examples of various types of comprehensions.
"""

# multiplication table as comprehension
list1 = [x * y for x in range(10) for y in range(10)]
print(list1)

# same code as above without comprehensions
list2 = []
for x in range(10):
    for y in range(10):
        list2.append(x * y)
print(list2)

list3 = []
for x in range(10):
    for y in range(10):
        list3.append((x, y))
print(map(lambda t: t[0] * t[1], list3))

# sets
print({x * 2 for x in range(10)})
print({2, 3, 4})

# dictionaries
print({2: 3, 4: 5})
print({x: x ** 2 for x in range(10)})

d = {"one": "one_value", "two": "two_value"}
print(dict((y, x) for x, y in d.items()))
