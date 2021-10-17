"""
This is an example showing how to create object hierarchies in python.

NOTES:
- inheriting from object is recommended (you get lots of methods)
- there are two ways to call parent methods.
- all methods are overload-able.
- parent attributes are directly accessible from the child
    (no access control).
- the "dir" function could be used for debugging.
"""


class A:
    def __init__(self, p_a):
        print("A.__init__")
        self.a = p_a

    def method_overloaded1(self):
        print("A.method_overloaded1")

    def method_overloaded2(self):
        print("A.method_overloaded2")

    def method_overloaded3(self):
        print("A.method_overloaded3")

    def method_overloaded4(self):
        print("A.method_overloaded4")

    def method_only_a(self):
        print("A.method_only_a")
        print(f"a is {self.a}")


class B(A):
    def __init__(self, p_b, p_a):
        print("B.__init__")
        # this is one way to call the parent constructor
        A.__init__(self, p_a)
        # super(self.__class__,self).__init__()
        self.b = p_b

    def method_overloaded1(self):
        """ the best way """
        print("B.method_overloaded1")
        super().method_overloaded1()

    def method_overloaded2(self):
        """ this is a second way to call the parent method """
        print("B.method_overloaded2")
        # pylint: disable=super-with-arguments
        super(B, self).method_overloaded2()

    def method_overloaded3(self):
        """
        The old way to call the parent method
        (no hard coding of the class name as above)
        """
        print("B.method_overloaded3")
        # pylint: disable=bad-super-call
        super(self.__class__, self).method_overloaded3()

    def method_overloaded4(self):
        """ This is going back to the first way """
        print("B.method_overloaded4")
        A.method_overloaded4(self)

    def method_only_b(self):
        print("B.method_only_b")
        print(f"a is {self.a}")
        print(f"b is {self.b}")


a = A(6)
print(f"dir(a) is {dir(a)}")
print("=================================")
b = B(5, 8)
print(f"dir(b) is {dir(b)}")
print("=================================")
b.method_only_a()
b.method_overloaded1()
b.method_overloaded2()
b.method_overloaded3()
b.method_overloaded4()
b.method_only_b()
