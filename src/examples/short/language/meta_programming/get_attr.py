"""
This is an example of overloading the __getattr__ python method. This allows
one to pretend to have various attributes or to decide that attributes
come in and out of scope at runtime. Uses for this could include:
- testing and simulation of errors.
- Aspect Oriented Programming.
- Proxy implementations.
- ORM solutions.
- Backwards compatibility solutions.
And more...
"""

from typing import Any


class A:
    def __init__(self) -> None:
        pass
        # self.d={}  # noqa: ERA001  teaching: kept in the comment for the reader

    def __getattr__(self, name: str):
        return name[::-1]
        # def my_method(self):
        #    print("in here with name",name)  # noqa: ERA001  teaching: kept in the comment for the reader
        # return my_method  # noqa: ERA001  teaching: kept in the comment for the reader

    def __setattr__(self, name: str, val: Any) -> None:
        # print("ERROR! dont touch this...")  # noqa: ERA001  teaching: kept in the comment for the reader
        # getattr(self,"d").__setitem__("\""+name+"\"",val)  # noqa: ERA001  teaching: kept in the comment for the reader
        pass


a = A()
print(dir(a))
print(a.whatIsThis)
print(a.whatsGoingOn)
print(a.howManyAttributesDoesThisObjectHave)
# a.my_private=7  # noqa: ERA001  teaching: kept in the comment for the reader
