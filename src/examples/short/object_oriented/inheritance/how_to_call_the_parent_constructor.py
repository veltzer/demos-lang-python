"""
This is an example showing how to create object hierarchies in python.

NOTES:
- inheriting from object is not needed in python3.
- there are several ways to call parent constructor (see the notes).

References:
- https://stackoverflow.com/questions/2399307/how-to-invoke-the-super-constructor-in-python
- https://stackoverflow.com/questions/12557612/calling-a-parent-class-constructor-from-a-child-class-in-python
- https://stackoverflow.com/questions/904036/chain-calling-parent-initialisers-in-python
"""


class A:
    def __init__(self):
        self.a = 5


class B1(A):
    """ most standard and short way """

    # pylint: disable=useless-super-delegation
    def __init__(self):
        super().__init__()


class B2(A):
    """ If you don't need to do anything in your constructor, you get your fathers """


class B3(A):
    """ This works but hardcodes the parent class yet again """

    def __init__(self):
        A.__init__(self)


class B4(A):
    """ python2 way """

    # pylint: disable=useless-super-delegation
    def __init__(self):
        # pylint: disable=super-with-arguments
        super(B4, self).__init__()


class B5(A):
    """ python2 way but without coding the class name yet again """

    # pylint: disable=useless-super-delegation
    def __init__(self):
        # pylint: disable=bad-super-call
        super(self.__class__, self).__init__()


b1 = B1()
b2 = B2()
b3 = B3()
b4 = B4()
b5 = B5()
assert b1.a == 5
assert b2.a == 5
assert b3.a == 5
assert b4.a == 5
assert b5.a == 5
