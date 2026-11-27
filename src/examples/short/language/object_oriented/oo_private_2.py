"""
This example shows that private values (values stored in attributes
whose names is prefixed by one or two underscores) are not really private.
- _values can be changed as is.
- __values are just hidden in funny names. The reason for this is inheritance.

NOTE: new style (deriving from "object") type object or old style object make no
difference as to this point.
"""


class Book:
    def __init__(self, price: int, name: str) -> None:
        self.__price = price
        self._name = name

    def print_me(self) -> None:
        print("price is", self.__price)
        print("name is", self._name)

    def set_price(self, price: int) -> None:
        self.__price = price

    def get_price(self):
        return self.__price

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self):
        return self._name


b = Book(50, "Lord of the Rings")
b.print_me()
# lets try to change the __price attribute directly...
# Notice that we get an exception not because the attribute is "private"
# but rather because such an attribute really DOES NOT exist...
try:
    print(f"price is {b.__price}")  # pyrefly: ignore[no-access]  teaching: shows that name mangling is not real privacy  # noqa: SLF001  teaching: shows that underscore names are not real privacy
except AttributeError:
    print("You see,you cannot directly change an attribute which does not exist")
# We CAN change the name since attributes that have just one _ in front of them appear AS IS
# in the object
print("if you see hobbit below it means we changed the attribute even though it has _ in front of it")
b._name = "hobbit"  # noqa: SLF001  teaching: shows that underscore names are not real privacy
b.print_me()

# Now lets see what the object really has...
print(dir(b))

# OK. I got it,the object really has the "_Book__price" attribute. Lets see if we can change
# that... YES WE CAN...
print("if you see price=70 it means we changed the attribute even though it has __ in front of it")
b._Book__price = 70  # pyrefly: ignore[missing-attribute]  teaching: name mangling is not security  # noqa: SLF001  teaching: shows that underscore names are not real privacy
b.print_me()
