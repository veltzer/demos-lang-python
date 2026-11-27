"""
This exapmle examines how jsonpickle serializes a python list
"""


import jsonpickle


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Person: name={self.name}, age={self.age}"

    def __eq__(self, other: object):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age

    def __hash__(self) -> int:
        return hash((self.name, self.age))


# Create an instance of the class
o1 = Person("John", 30)
o2 = Person("Mary", 24)
l1 = [o1, o2]
print(l1)

# Serialize the instance to JSON using jsonpickle
json_str = jsonpickle.encode(l1)
print(json_str)

l2 = jsonpickle.decode(json_str)
print(l2)

print(l1 == l2)
