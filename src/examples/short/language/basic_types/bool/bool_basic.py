"""
A basic demo of booleans
"""

# create a boolean
b = bool()  # noqa: UP018  teaching: demonstrating the constructor call
assert b is False
assert type(b) is bool

if False:
    print("You shouldnt see this")
if True:
    print("You should see this")
if 0:
    print("You shouldnt see this")
if 1:  # pyrefly: ignore[redundant-condition]  teaching: the truthiness of an int literal is the lesson
    print("You should see this")
if []:
    print("You shouldnt see this")
if ["one"]:
    print("You should see this")
