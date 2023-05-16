"""
This example shows how to print a traceback
"""
from traceback import print_exc


try:
    raise ValueError("hello")
except ValueError:
    print_exc()
