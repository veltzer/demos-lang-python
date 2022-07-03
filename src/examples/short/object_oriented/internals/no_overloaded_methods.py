# type: ignore
"""
This example plainly shows that you cannot have two methods in a class by the same
name. This is true for constructors as well as for regular methods.
"""
from pyfakeuse import fake_use


class A:
    def __init__(self, val):
        self.__private_var = val

    # noinspection PyRedeclaration
    # pylint: disable=function-redefined
    def __init__(self):  # noqa: F811
        self.__private_var = 5

    def sayHello(self):
        print(self.__private_var, 'hello')

    # noinspection PyRedeclaration
    def sayHello(self, name):  # noqa: F811
        print(self.__private_var, 'hello', name)


try:
    # pylint: disable=too-many-function-args
    a = A(5)
    fake_use(a)
except TypeError:
    print('oops,got an error')
    print('the no argument version of the constructor does not exist...')
# this will pass without an exception...
a = A()
try:
    a.sayHello()
except TypeError:
    print('oops,got an error')
    print('the no argument version of the method \'sayHello\' does not exist')
# pylint: disable=too-many-function-args
a.sayHello('mark')
