"""
An example showing the different ways to create dicts

Notes:
- there are many ways to create dicts
- most of the time you don't need to code a loop to create your dictionary

TODO:
- from help(dict) it seems that there should be a way to create a dictionary
from a mapping object. I need to add an example of this.
"""


def gen_tuples():
    for i in range(5):
        yield i, i + 1


list_of_tuples = [(3, 4), (5, 6), (7, 8)]
list_of_keys = ['red', 'green', 'blue']
list_of_values = ['red', 'green', 'blue']

# simplest way, built in the language syntax, empty dictionary
d1 = {}
print(d1)
# explicit dictionary syntax with some data
d2 = {"one": "two", "three": "four"}
print(d2)
# empty constructor -> empty dictionary
d3 = dict()
print(d3)
# constructor with key, value pairs to initialize the dictionary
d4 = dict(one='two', three='four')
print(d4)
# copy
d5 = dict(d1)
print(d5)
# comprehension
d6 = {x: x * x for x in range(5)}
print(d6)
# dict.fromkeys
d7 = dict.fromkeys(range(5), "foo")
print(d7)
# any generator that return tuples
d8 = dict(gen_tuples())
print(d8)
# any container of tuples
d9 = dict(list_of_tuples)
print(d9)
# use zip to construct a dictionary from anything iterable as keys and anything iterable as values
d10 = dict(zip(list_of_keys, range(3)))
print(d10)
# use enumerate to create a dictionary with the indexes as keys for something iterable
# there is a type problem here and that's why we override pycharm's type checking
# noinspection PyTypeChecker
d11 = dict(enumerate(list_of_values))
print(d11)
