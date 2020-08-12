"""
Sometimes you want to iterate tuples and you dont want all members.
Here is how you do it.

Notes:
- the underscore is actually a variable name so its use has no bearing on performance.
- the underscore is a convention only in python, not core language feature.
- you can even use the value of the underscore since it is a regular variable.
- it is however non-descriptive and on code review it will be evident that you are not interested
in that position within the tuple.
- note that you cannot do something like 'for (x,,y) in tuples' as it will not compile

References:
http://stackoverflow.com/questions/3061336/how-can-i-iterate-over-only-the-first-variable-of-a-tuple
"""

tuples = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12),
]

for (x, _, y) in tuples:
    print(x, y)
