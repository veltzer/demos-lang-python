"""
This example shows the problem with mutable default values.

What is the issue?
The default value is evaluated only once and is like a global
variable which is mutable.
"""


# pylint: disable=dangerous-default-value
def add_name(name: str, target: list[str] = []) -> list[str]:
    target.append(name)
    return target


print(add_name("Alice"))
print(add_name("Bob"))
print(add_name("Charlie"))
