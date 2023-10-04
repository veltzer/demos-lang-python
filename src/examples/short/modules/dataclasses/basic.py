"""
A basic example of data classes

Compare doing the object with and without the @dataclass decorator.
"""

from dataclasses import dataclass


# without dataclass
class PersonManual:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name}, {self.address}"


@dataclass
class PersonData:
    """
    __init__ and __str__ is automatically generated
    """
    name: str
    address: str


pm = PersonManual(name="Mark", address="Israel")
print(pm)
pd = PersonData(name="Mark", address="Israel")
print(pd)
