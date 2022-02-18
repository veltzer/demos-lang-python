"""
This is a simple example of writing a python function decorator

References:
- https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
"""

import random


def sum_10(func):
    def inner():
        sum = 0
        for i in range(10):
            sum += func()
        return sum
    return inner

@sum_10
def return_some_number():
    return random.random()

@sum_10
def return_1():
    return 1

print(return_some_number())
print(return_1())
