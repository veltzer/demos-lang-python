#!/usr/bin/env python

"""
This is an example of creating your own resource to be used with the 'with'
python syntax. This is called a 'Context Manager'.

You can see the basic flow of code:
- first the constructor of your context manager is called.
- then your __enter__ code is called.
- then the users code block is executed.
- then your __exit__ code is called.
"""


class MyResource:

    def __init__(self, name):
        self.name = name
        print("{} constructor".format(self.name))

    def __enter__(self):
        print("{} enter".format(self.name))

    def __exit__(self, itype, value, traceback):
        print("{} exit".format(self.name))


with MyResource("r1") as r1, MyResource("r2") as r2:
    print("block of code")
