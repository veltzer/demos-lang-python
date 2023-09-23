"""
This example shows the python types associated with python objects.
"""

with open("/etc/passwd") as f:
    print(type(f))
    print(super(type(f)))
