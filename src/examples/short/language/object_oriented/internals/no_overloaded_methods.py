"""
This example plainly shows that you cannot have two methods in a class by the same
name. This is true for constructors as well as for regular methods.
"""



class A:
    def __init__(self, val):
        self.__private_var = val

    # noinspection PyRedeclaration
    # pylint: disable=function-redefined
    def __init__(self):  # type: ignore[no-redef] # noqa: F811
        self.__private_var = 5

    def say_hello(self):
        print(self.__private_var, "hello")

    # noinspection PyRedeclaration
    def say_hello(self, name):  # noqa: F811  teaching: python has no overloading, the second def replaces the first
        print(self.__private_var, "hello", name)


try:
    # pylint: disable=too-many-function-args
    a = A(5)  # pyrefly: ignore[bad-argument-count]
except TypeError:
    print("oops,got an error")
    print("the no argument version of the constructor does not exist...")
# this will pass without an exception...
a = A()  # type: ignore[call-arg]
try:
    # pylint: disable=no-value-for-parameter
    a.say_hello()  # pyrefly: ignore[missing-argument]  teaching: the no argument version does not exist
except TypeError:
    print("oops,got an error")
    print("the no argument version of the method \"say_hello\" does not exist")
# pylint: disable=too-many-function-args
a.say_hello("mark")
