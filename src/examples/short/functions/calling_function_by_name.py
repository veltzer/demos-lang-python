"""
This example shows how you can call a function when all you
know is its name. The name may come from the user, database, etc.
The idea here is to use 'vars()[name]' to get the function object
and then just apply the '()' or '__call__' method on it.
"""


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


name = input('give me the name off the function: ')
num = int(input('how many arguments to pass to the function: '))
str_list = []
for i in range(num):
    a = input(f"give me argument [{i}]: ")
    str_list.append(a)
# these two are the same
print((vars()[name])(*str_list))
# pylint: disable=unnecessary-dunder-call
print((vars()[name]).__call__(*str_list))
