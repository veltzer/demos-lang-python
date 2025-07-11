"""
This example plainly shows that you cannot have two methods in a class by the same
name. This is true for constructors as well as for regular methods.
"""
# type: ignore


class A:
    def __init__(self, val):
        self.__private_var = val

    # noinspection PyRedeclaration
    # pylint: disable=function-redefined
    # noqa: F811
    def __init__(self):  # type: ignore[no-redef]
        self.__private_var = 5

    def sayHello(self):
        print(self.__private_var, "hello")

    # noinspection PyRedeclaration
    # noqa: F811
    def sayHello(self, name):  # type: ignore[no-redef]
        print(self.__private_var, "hello", name)


try:
    # pylint: disable=too-many-function-args
    a = A(5)
except TypeError:
    print("oops,got an error")
    print("the no argument version of the constructor does not exist...")
# this will pass without an exception...
a = A()  # type: ignore[call-arg]
try:
    # pylint: disable=no-value-for-parameter
    a.sayHello()
except TypeError:
    print("oops,got an error")
    print("the no argument version of the method \"sayHello\" does not exist")
# pylint: disable=too-many-function-args
a.sayHello("mark")  # type: ignore[call-arg]
