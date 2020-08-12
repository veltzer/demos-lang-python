"""
This example demonstrates that an object is just a dictionary and you can access it's
underlying dictionary via the __dict__ attribute and see all of it's attributes there.
It also shows that the class itself is also an object and anything you write at the
class level is in that object.
The __dict__ both for the instances and for the class is public and so can be accessed
from outside the class.
"""


class A:
    pi = 3.14

    def __init__(self, val):
        print('in A constructor')
        self.a = val

    def printMe(self):
        print('a is', self.a)


a = A(7)
print('dir(a) follows...')
print(dir(a))
print('a.__dict__ follows...')
print(a.__dict__)
print('A.__dict__ follows...')
print(A.__dict__)
