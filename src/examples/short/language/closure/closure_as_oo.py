"""
An example showing how, to some extent closure can be seen as a replacement
for object oriented programming. The "person" function below could
be seen as a sort of constructor.
"""


def person(initial_name, initial_age):
    o = {
        "name": initial_name,
        "age": initial_age,
    }

    def get_name():
        return o["name"]

    def set_name(name):
        o["name"] = name

    def get_age():
        return o["age"]

    def set_age(age):
        o["age"] = age

    return {
        "get_name": get_name,
        "set_name": set_name,
        "get_age": get_age,
        "set_age": set_age,
    }


p = person("Bilbo", 111)
p["set_age"](112)
print("age is", p["get_age"]())
p2 = person("Frodo", 77)
p2["set_age"](78)
print("age is", p2["get_age"]())
