"""
This example demonstrates the "match" statement in python
"""


def check_type(value):
    match value:
        case int():
            print(f"{value} is an integer")
        case str():
            print(f"{value} is a string")
        case list():
            print(f"{value} is a list with {len(value)} elements")
        case dict():
            print(f"{value} is a dictionary with {len(value)} key-value pairs")
        case _:
            print(f"{value} is of an unknown type")


# Test the function with different types
check_type(42)
check_type("Hello")
check_type([1, 2, 3])
check_type({"a": 1, "b": 2})
check_type(3.14)
