"""
This example explores how jsonpickle serializes instances of classes
"""

import jsonpickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: name={self.name}, age={self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


# Create an instance of the class
o1 = Person("John", 30)
print(o1)

# Serialize the instance to JSON using jsonpickle
json_str = jsonpickle.encode(o1)
print(json_str)

o2 = jsonpickle.decode(json_str)
print(o2)

print(o1 == o2)
