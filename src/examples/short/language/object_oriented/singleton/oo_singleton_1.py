"""
This is an example of a singleton pattern in python.
Notice that since we cannot make the constructor private
we resort to making sure,inside the constructor code,
that we are not called a second time.

This example is not that pretty in that it does not use a
"real" static method of the A class to return the singleton
instance. See the next example for an improvement on this.

This "get_instance" method is also not protected against multi
thread access. Again,see next examples for a more realistic
solution.

The problem with this example is that you can call the
constructor for A * without * the "get_instance" method
(simply by a=A()) and in this case it will not be registered
as the instance (in A.instance). This can be fixed by moving
the registration into the constructor function itself.
"""
from typing import Any, ClassVar


class A:
    instance: ClassVar[Any | None] = None

    def __init__(self) -> None:
        if A.instance is not None:
            raise ValueError("you called the constructor twice!!")
        # constructor code goes here
        print("in A constructor")
        self.my_attribute = "value"


def get_instance() -> A:
    if A.instance is None:
        A.instance = A()
    return A.instance


my_a1 = get_instance()
my_a2 = get_instance()
if my_a1 is my_a2:
    print("yes,they are the same instance")
print(dir(my_a1))
