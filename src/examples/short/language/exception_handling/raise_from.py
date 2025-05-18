"""
This example shows how to use the python "raise from" syntax.
This syntax enables you to raise an exception with a cause exception
attached to that exception.

Compare the output of the next two errors to understand with you
should use the "raise from" syntax.

References:
- https://www.pythontutorial.net/python-oop/python-raise-from
"""


def correct_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError("b must not be zero") from ex


def incorrect_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        # pylint: disable=raise-missing-from
        raise ValueError("b must not be zero")


# correct_divide(10, 0)
incorrect_divide(10, 0)
