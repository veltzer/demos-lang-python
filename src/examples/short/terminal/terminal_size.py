"""
A program that shows you how to get the size of the terminal.

A clear winner in terms of performance is the ioctl(2) one.

References:
http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
"""

import fcntl
import os
import struct
import termios
import timeit


def terminal_size1():
    h, w, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)), )
    return w, h


terminal_size1.name = 'ioctl'


def terminal_size2():
    ret = os.popen('stty size').read().split()
    return int(ret[1]), int(ret[0])


terminal_size2.name = 'stty'


def terminal_size3():
    x = int(os.popen('tput cols').read())
    y = int(os.popen('tput lines').read())
    return x, y


terminal_size3.name = 'tput'


def terminal_size4():
    d = {}
    for tc_entry in os.environ['TERMCAP'].split(':'):
        if tc_entry.find('#') != -1:
            key, val = tc_entry.split('#')
            d[key] = val
    return int(d['co']), int(d['li'])


terminal_size4.name = 'TERMCAP'


def terminal_size5():
    """ this function does not work since LINES and COLUMNS are not exported"""
    x = int(os.environ['LINES'])
    y = int(os.environ['COLUMNS'])
    return x, y


terminal_size5.name = 'environment'

print(terminal_size1())
print(terminal_size2())
print(terminal_size3())
print(terminal_size4())
# print(terminal_size5())

functions = [
    terminal_size1,
    terminal_size2,
    terminal_size3,
    terminal_size4,
    #    terminal_size5,
]

number = 1000
results = [(timeit.timeit(f, number=number), f.name) for f in functions]
sorted_results = sorted(results, key=lambda tup: tup[0])
for r in sorted_results:
    print('{0:.4f}: {1}'.format(r[0], r[1]))
