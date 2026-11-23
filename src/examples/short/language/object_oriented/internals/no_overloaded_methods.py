"""
This example plainly shows that you cannot have two methods in a class by the same
name. This is true for constructors as well as for regular methods.
"""



class A:
    def __init__(self, val):
        self.__private_var = val

    # noinspection PyRedeclaration
    def __init__(self):  # noqa: F811  teaching: the second definition deliberately replaces the first
        self.__private_var = 5

    def say_hello(self):
        print(self.__private_var, "hello")

    # noinspection PyRedeclaration
    def say_hello(self, name):  # noqa: F811  teaching: the second definition deliberately replaces the first
        print(self.__private_var, "hello", name)


try:
    a = A(5)  # pyrefly: ignore[bad-argument-count]  teaching: the second __init__ replaced the first, so this call fails
except TypeError:
    print("oops,got an error")
    print("the no argument version of the constructor does not exist...")
# this will pass without an exception...
a = A()
try:
    a.say_hello()  # pyrefly: ignore[missing-argument]  teaching: the no argument version does not exist
except TypeError:
    print("oops,got an error")
    print("the no argument version of the method \"say_hello\" does not exist")
a.say_hello("mark")
