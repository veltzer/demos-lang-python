"""
A basic demo of booleans
"""

# create a boolean
b = bool()  # noqa: UP018 - demonstrating the bool() constructor
assert b is False
# pylint: disable=unidiomatic-typecheck
assert type(b) is bool

# pylint: disable=using-constant-test
if False:
    print("You shouldnt see this")
# pylint: disable=using-constant-test
if True:
    print("You should see this")
# pylint: disable=using-constant-test
if 0:
    print("You shouldnt see this")
# pylint: disable=using-constant-test
if 1:  # pyrefly: ignore[redundant-condition]
    print("You should see this")
# pylint: disable=using-constant-test
if []:
    print("You shouldnt see this")
# pylint: disable=using-constant-test
if ["one"]:
    print("You should see this")
