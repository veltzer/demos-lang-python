"""
This is an example of how to get a value back from a piece
of code you execute with the "exec" function.
"""

d = {}  # type: ignore
# pylint: disable=exec-used
exec("ret=7", {}, d)
print(d["ret"])
