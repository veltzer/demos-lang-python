#!/usr/bin/python3

from module import *

a()
try:
    b()
except NameError as _:
    print("yes got exception")
