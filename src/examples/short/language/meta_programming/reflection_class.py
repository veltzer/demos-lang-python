"""
This shows how to know the class that you are in...
"""


class A:
    def print_my_class(self):
        print(self.__class__)


a = A()
# this is pretty straight forward
assert isinstance(a, A)
# every object is of type "object"
assert isinstance(a, object)
# every type if of type "type"
assert isinstance(a.__class__, type)
a.print_my_class()
