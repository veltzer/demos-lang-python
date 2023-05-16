"""
This is an example of how to do a weighted choice/sample using the
    numpy.random.choice API.

NOTES:
- the weights must sum up to 1.0 otherwise you will get the error:
    ValueError: probabilities do not sum to 1
- if replace=False (this is not the default) then you have to make sure
    that len(elements)=>size and then you get unique selection of elements.

References:
- https://stackoverflow.com/questions/10803135/weighted-choice-short-and-simple
"""

from numpy.random import choice

elements = ["one", "two", "three"]
weights = [0.2, 0.3, 0.5]

# replate=True is the default
print(choice(elements, p=weights, size=20, replace=True))
print(choice(elements, p=weights, size=20, replace=False))
