"""
This example shows how to convert unicode to ascii in python.

The solution here is to convert to ascii and ignore all errors.
Not the best solution but OK for some cases.

This works in python2 also...

References:
- http://stackoverflow.com/questions/4299675/python-script-to-convert-from-utf-8-to-ascii
- http://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii
"""

s = "\u05d4\u05d9hello"
print(type(s))
print(s)

r = s.encode("ascii", errors="ignore").decode("utf8")
print(type(r))
print(r)

r = s.encode("ascii", errors="ignore").decode()
print(type(r))
print(r)

r = "".join(c for c in s if ord(c) < 128)
print(type(r))
print(r)

r = s.encode(errors="ignore").decode()
print(type(r))
print(r)
