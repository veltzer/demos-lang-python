"""
This is an example showing how to create object hierarchies in python.

NOTES:
- inheriting from object is recommended (you get lots of methods)
- there are two ways to call parent methods.
- all methods are overloadable.
- parent attributes are directly accessible from the child
    (no access control).
- the 'dir' function could be used for debugging.
"""


class A:
    def __init__(self, p_a):
        print('A.__init__')
        self.a = p_a

    def method_overloaded1(self):
        print('A.method_overloaded1')

    def method_overloaded2(self):
        print('A.method_overloaded2')

    def method_overloaded3(self):
        print('A.method_overloaded3')

    def method_onlya(self):
        print('A.method_onlya')
        print('a is', self.a)


class B(A):
    def __init__(self, p_b, p_a):
        print('B.__init__')
        # this is one way to call the parent constructor
        A.__init__(self, p_a)
        # super(self.__class__,self).__init__()
        self.b = p_b

    def method_overloaded1(self):
        print('B.method_overloaded1')
        # this is a second way to call the parent method
        super(B, self).method_overloaded1()

    def method_overloaded2(self):
        print('B.method_overloaded2')
        # this is the best way to call the parent method
        # (no hardcoding of the class name as above)
        super(self.__class__, self).method_overloaded2()

    def method_overloaded3(self):
        print('B.method_overloaded3')
        # This is going back to the first way
        A.method_overloaded3(self)

    def method_onlyb(self):
        print('B.method_onlyb')
        print('a is', self.a)
        print('b is', self.b)


a = A(6)
print('dir(a) is')
print(dir(a))
print('=================================')
b = B(5, 8)
print('dir(b) is')
print(dir(b))
print('=================================')
b.method_onlya()
b.method_overloaded1()
b.method_overloaded2()
b.method_overloaded3()
b.method_onlyb()
