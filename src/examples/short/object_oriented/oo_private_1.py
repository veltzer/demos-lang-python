"""
This demo explores the meaning of 'private' members in python (__).

The end result is that you can override both _ and __ values in
python.
"""


class MyClass:
    def __init__(self):
        self.public_variable = 5
        self.__private_variable = 5

    def pr(self):
        print("printing")
        print(f"public_variable is {self.public_variable}")
        print(f"__private_variable is {self.__private_variable}")

    # this demonstrates that you dont have to call 'self' as 'self',its just
    # a convention

    def setPrivate(self, val):
        self.__private_variable = val

    def setPublic(self, val):
        self.public_variable = val


print('constructing')
b = MyClass()
print('printing the newly constructed class')
b.pr()
print('setting accessible variable')
b.public_variable = 4
b.pr()
print('and with a method')
b.setPublic(9)
b.pr()
print('and another way to call the same method')
MyClass.setPublic(b, 11)
b.pr()
print('here is how you access the accessible variable ' + str(b.public_variable))
print('setting inaccessible variable')
# pylint: disable=protected-access
b.__private_variable = 6
b.pr()
print('didnt work,huh ?')
print('from outside its value looks like ' + str(b.__private_variable))
# noinspection PyProtectedMember
print('this is our real var ' + str(b._MyClass__private_variable))  # type: ignore
print('this means that there is no real security for the __[var] in python')
print('lets look at our class')
# pylint: disable=attribute-defined-outside-init
b._MyClass__private_variable = 666  # type: ignore
b.pr()
b.pr()
print(dir(MyClass))
print(dir(MyClass.__module__))
