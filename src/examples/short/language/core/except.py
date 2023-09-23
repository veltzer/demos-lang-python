"""
Example code for raising an exception,catching it and executing finally code in python.
"""

try:
    raise ValueError("hello")
except ValueError as e:
    print("in except", e)
finally:
    print("finally is here")
