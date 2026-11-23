"""
This example shows the problem with mutable default values.

What is the issue?
The default value is evaluated only once and is like a global
variable which is mutable.
"""


def add_name(name: str, target: list[str] = []) -> list[str]:  # noqa: B006  teaching: the shared mutable default is the lesson
    target.append(name)
    return target


def add_name_fixed(name: str, target: list[str] | None = None) -> list[str]:
    if target is None:
        target = []
    target.append(name)
    return target


print(add_name("Alice"))
print(add_name("Bob"))
print(add_name("Barbie", target=[]))
print(add_name("Charlie"))
print("now for the fixed version")
print(add_name_fixed("Alice"))
print(add_name_fixed("Bob"))
print(add_name_fixed("Barbie", target=[]))
print(add_name_fixed("Charlie"))
