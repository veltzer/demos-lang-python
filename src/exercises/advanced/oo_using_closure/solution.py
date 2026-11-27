"""
solution.py
"""

from types import SimpleNamespace


def person(name: str, age: int) -> SimpleNamespace:
    data = SimpleNamespace()

    def set_name(name: str) -> None:
        data.__dict__["name"] = name

    def get_name():
        return data.name

    def set_age(age: int) -> None:
        if age <= 0:
            raise ValueError("age error")
        data.__dict__["age"] = age

    def get_age():
        return data.age

    def print_me() -> None:
        print("name is ", data.name)
        print("age is ", data.age)

    data.set_name = set_name
    data.get_name = get_name
    data.set_age = set_age
    data.get_age = get_age
    data.print_me = print_me
    set_name(name)
    set_age(age)
    return data


# usage...
p1 = person("mark", 36)
p2 = person("doron", 32)
print(p1.name)
p1.print_me()
p2.print_me()
p1.set_name("foobar")
p1.set_age(74)
p1.print_me()
