"""
A basic demo of booleans
"""

# create a boolean
b=bool()
assert b is False
assert type(b)==bool

if False:
    print("You shouldnt see this")
if True:
    print("You should see this")
if 0:
    print("You shouldnt see this")
if 1:
    print("You should see this")
if []:
    print("You shouldnt see this")
if ["one"]:
    print("You should see this")
