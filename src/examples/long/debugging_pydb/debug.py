"""
This is an example of a simple python application
that you can use to debug with pydb.
"""


def calc():
    i = 0
    current_sum = 0
    while True:
        current_sum += i
        i += 1


calc()
