"""
This demo explores the meaning of "private" members in python (__).

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

    # this demonstrates that you dont have to call "self" as "self",its just
    # a convention

    def set_private(self, val):
        self.__private_variable = val

    def set_public(self, val):
        self.public_variable = val


print("constructing")
b = MyClass()
print("printing the newly constructed class")
b.pr()
print("setting accessible variable")
b.public_variable = 4
b.pr()
print("and with a method")
b.set_public(9)
b.pr()
print("and another way to call the same method")
MyClass.set_public(b, 11)
b.pr()
print("here is how you access the accessible variable " + str(b.public_variable))
print("setting inaccessible variable")
b.__private_variable = 6  # noqa: SLF001  teaching: shows that name mangling is not real privacy
b.pr()
print("didnt work,huh ?")
print("from outside its value looks like " + str(b.__private_variable))  # pyrefly: ignore[no-access]  teaching: shows that name mangling is not real privacy  # noqa: SLF001  teaching: shows that name mangling is not real privacy
# noinspection PyProtectedMember
print("this is our real var " + str(b._MyClass__private_variable))  # pyrefly: ignore[missing-attribute]  teaching: name mangling is not security  # noqa: SLF001  teaching: shows that name mangling is not real privacy
print("this means that there is no real security for the __[var] in python")
print("lets look at our class")
b._MyClass__private_variable = 666  # pyrefly: ignore[missing-attribute]  teaching: name mangling is not security  # noqa: SLF001  teaching: shows that name mangling is not real privacy
b.pr()
b.pr()
print(dir(MyClass))
print(dir(MyClass.__module__))
