"""
This shows basic assertions in python

Notes:
- you can use assertions without informative messages like so
    assert 2 + 2 == 4
- you can use assertions with informative message like so
    assert 2 + 2 == 5, "this should always raise exceptions"
- when an assert fails you get an "AssertionError" exception.
- if you add an informative message to your assertion than
    the user will get that message as the first element of the
    e.args tuple when he gets an assertion.
"""

assert 2 + 2 == 4
try:
    assert 2 + 2 == 5, "some text"
except AssertionError as e:
    print(dir(e))
    print("yes, 2+2 != 5")
    print(e.args)
# assert with text
assert 2 + 5 == 6, "nope, thats wrong"
