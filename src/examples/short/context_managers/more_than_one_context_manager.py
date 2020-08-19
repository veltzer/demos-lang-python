"""
This is an example of how to use more than one context manager at a time...

References:
- https://stackoverflow.com/questions/893333/multiple-variables-in-a-with-statement
"""


class MyResource:

    def __init__(self, name):
        self.name = name
        print("{} constructor".format(self.name))

    def __enter__(self):
        print("{} enter".format(self.name))

    def __exit__(self, _type, value, traceback):
        print("{} exit".format(self.name))


with MyResource("r1") as r1, MyResource("r2") as r2:
    print("block of code")
