"""
This is a simple example of how to call the "exec" function
"""

d = {}
exec("ret=7", {}, d)
print(d["ret"])
