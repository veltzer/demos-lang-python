"""
This example shows how to generically call a function you know nothing about
and get the arguments for it from the outside
"""


def call_n_times(n, f, *args, **kwargs):
    for i in range(n):
        f(*args, **kwargs)


def print_string(s):
    print(s)


call_n_times(5, print_string, 'mark')
