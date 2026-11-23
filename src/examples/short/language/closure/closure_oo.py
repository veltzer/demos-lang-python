"""
This is an example of how to use the closure feature to do some
oo work.
Notice:
- We treat the "person" function as a constructor.
- We call it with a capital first letter.
- We pass arguments to it needed to create the instance.
- In order to have lots of data in the closure we simply
store a flexible and big data structure in the closure (in this
case a dictionary).
- Because we want to return many methods and dont want tuples with
dozens of elements we return all method pointers in a dictionary as
well.
B This allows the user to call our methods by name instead of by
position in some returned tuple.
"""


# noinspection PyPep8Naming
def person(initial_name, initial_age):
    data = {
        "name": initial_name,
        "age": initial_age,
    }

    def set_name(name):
        data["name"] = name

    def get_name():
        return data["name"]

    def set_age(age):
        data["age"] = age

    def get_age():
        return data["age"]

    def print_me():
        print("name", data["name"])
        print("age", data["age"])

    return {
        "set_name": set_name,
        "get_name": get_name,
        "set_age": set_age,
        "get_age": get_age,
        "print_me": print_me,
    }


p1 = person("Bilbo", 111)
p1["set_name"]("Sam")
p1["print_me"]()
p2 = person("Frodo", 33)
p2["set_name"]("Mary")
p2["print_me"]()
p1["print_me"]()
